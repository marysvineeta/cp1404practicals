"""CP1404/CP5632 Practical - More Guitars."""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from file, display, add new ones, and save to file."""
    guitars = load_guitars(FILENAME)

    print("These are my guitars:")
    display_guitars(guitars)

    # Sort by year and display
    guitars.sort()
    print("\nThese are my guitars (sorted by year):")
    display_guitars(guitars)

    # Add new guitars from user
    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)

    # Save all guitars back to file
    save_guitars(FILENAME, guitars)
    print(f"\n{len(guitars)} guitars saved to {FILENAME}.")


def load_guitars(filename):
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            name, year, cost = line.split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_string}")


def get_new_guitars():
    print("\nAdd new guitars (leave name blank to finish):")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
