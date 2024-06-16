
def main():

    incomes = []
    number_of_month = int(input("How many months? "))

    for month in range(1, number_of_month + 1):
        income = float(input(f"Enter income for month {month} : "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    report_display(incomes, number_of_month)


def report_display(incomes, number_of_month):

    total = 0
    for month in range(1, number_of_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()