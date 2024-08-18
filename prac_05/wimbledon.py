import csv

def read_data(filename):
    """Read data from  CSV file."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return data


def count_champions(data):
    champions_count = {}
    for row in data:
        champion = row[2]  # Assuming the champion's name is in the third column
        champions_count[champion] = champions_count.get(champion, 0) + 1
    return champions_count


def extract_countries(data):
    countries = set()
    for row in data:
        country = row[1]  # Assuming the country is in the second column
        countries.add(country)
    sorted_countries = sorted(countries)
    return sorted_countries


def main():
    filename = "wimbledon.csv"
    data = read_data(filename)

    champions_count = count_champions(data)
    print("Wimbledon Champions:")
    for champion, count in champions_count.items():
        print(f"{champion} {count}")

    countries = extract_countries(data)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
