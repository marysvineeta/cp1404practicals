import csv
from guitar import Guitar


def main():
    guitars = load_guitars('guitars (1).csv')
    display_guitars(guitars, "Guitars loaded from file:")

    guitars.sort()
    display_guitars(guitars, "Guitars sorted by year:")

    guitars += get_new_guitars()
    save_guitars('guitars (1).csv', guitars)
    print("New guitars added and saved to file.")


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars, header):
    print(header)
    for guitar in guitars:
        print(guitar)
    print()


def get_new_guitars():
    new_guitars = []
    while True:
        name = input("Enter guitar name (or press Enter to stop): ")
        if not name:
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars


def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
