def main():
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print an income report """
    print("\nIncome Report\n-------------")
    total = 0
    for month_number, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month_number:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
