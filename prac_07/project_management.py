"""
CP1404 Practical - Project Management

Estimate: 120 minutes
Actual: ? minutes
"""

import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"


def main():
    print("Welcome to Pythonic Project Management")

    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").strip().upper()

        if choice == "L":
            filename = input("Filename to load projects from: ").strip()
            if filename:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save projects to: ").strip()
            if filename:
                save_projects(filename, projects)
                print(f"Projects saved to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            answer = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip().lower()
            if answer.startswith("y"):
                save_projects(DEFAULT_FILENAME, projects)
                print(f"Projects saved to {DEFAULT_FILENAME}")
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice")


def print_menu():
    """Print the main menu."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    projects = []
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            in_file.readline()  # skip header
            for line in in_file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")
                name = parts[0]
                start_date_string = parts[1]
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion_percentage = int(parts[4])

                start_date = datetime.datetime.strptime(start_date_string, DATE_FORMAT).date()
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with no projects.")
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-separated file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            start_string = project.start_date.strftime(DATE_FORMAT)
            print(f"{project.name}\t{start_string}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    incomplete_projects.sort()  # uses __lt__ (priority)
    complete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Ask for a date and show projects that start after that date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format")
        return

    filtered = [p for p in projects if p.starts_after(filter_date) or p.start_date == filter_date]
    filtered.sort(key=lambda p: p.start_date)

    for project in filtered:
        print(project)


def add_new_project(projects):
    """Add a new project from user input."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    if not name:
        print("Project name cannot be blank.")
        return

    date_string = input("Start date (dd/mm/yyyy): ").strip()
    try:
        start_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format")
        return

    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print(f"{project} added.")


def update_project(projects):
    """Update completion percentage and/or priority for a chosen project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        index = int(input("Project choice: "))
        project = projects[index]
    except (ValueError, IndexError):
        print("Invalid project choice")
        return

    print(project)
    new_completion = input("New Percentage: ").strip()
    if new_completion != "":
        try:
            project.completion_percentage = int(new_completion)
        except ValueError:
            print("Invalid percentage - value not changed")

    new_priority = input("New Priority: ").strip()
    if new_priority != "":
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid priority - value not changed")


if __name__ == "__main__":
    main()
