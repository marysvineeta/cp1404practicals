import random

# Constants
INITIAL_PRICE = 10.0
MIN_PRICE = 1.0          # changed from $0.01 to $1.00
MAX_PRICE = 100.0        # changed from $1000 to $100
MAX_INCREASE = 0.175     # changed from 10% to 17.5%
MAX_DECREASE = 0.05      # 5% decrease (unchanged)
FILENAME = "capitalist_conrad_output.txt"

def main():
    price = INITIAL_PRICE
    number_of_days = 0

    out_file = open(FILENAME, 'w')

    print(f"Starting price: ${price:,.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1

        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
            price *= (1 + price_change)
        else:
            price_change = random.uniform(0, MAX_DECREASE)
            price *= (1 - price_change)

        print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

    out_file.close()

if __name__ == "__main__":
    main()
