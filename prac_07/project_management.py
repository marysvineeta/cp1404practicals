"""
Project Management Program
"""

from project import Project
from datetime import datetime


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip the header
        for line in file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete_projects, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date > date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)


def add_new_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    completion = input("New Percentage: ")
    priority = input("New Priority: ")
    if completion:
        project.update_completion(int(completion))
    if priority:
        project.update_priority(int(priority))


def main():
    FILENAME = 'projects.txt'
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> """

    while True:
        choice = input(menu).upper()
        if choice == 'L':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.strptime(date_string, "%d/%m/%Y")
            filter_projects_by_date(projects, date)
        elif choice == 'A':
            project = add_new_project()
            projects.append(project)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_choice = input(f"Would you like to save to {FILENAME}? (Y/N) ").upper()
            if save_choice == 'Y':
                save_projects(FILENAME, projects)
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
