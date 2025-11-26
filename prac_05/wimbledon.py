"""
Wimbledon
Estimate: 35 minutes
Actual:   45 minutes
"""

import csv


def main():
    rows = load_wimbledon_data("wimbledon 2.csv")
    champion_to_wins = count_champions(rows)
    countries = get_countries(rows)

    print("Wimbledon Champions:")
    for champion in sorted(champion_to_wins):
        print(f"{champion} {champion_to_wins[champion]}")

    print()
    country_list = ", ".join(sorted(countries))
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(country_list)


def load_wimbledon_data(filename):
    """Load CSV into a list of lists (rows). Handles UTF-8 with BOM."""
    with open(filename, "r", encoding="utf-8-sig", newline="") as in_file:
        reader = csv.reader(in_file)
        header = next(reader)
        # Find columns by name so order can vary
        champion_index = header.index("Champion")
        country_index = header.index("Country")
        rows = []
        for row in reader:
            # Keep only needed columns in a compact row: [Champion, Country]
            rows.append([row[champion_index], row[country_index]])
        return rows


def count_champions(rows):
    """Return dict of champion -> number of wins."""
    champion_to_wins = {}
    for champion, _ in rows:
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_countries(rows):
    """Return a set of unique country codes from rows."""
    countries = set()
    for _, country in rows:
        countries.add(country)
    return countries


if __name__ == "__main__":
    main()
