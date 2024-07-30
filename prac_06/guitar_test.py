from guitar import Guitar  # Assuming Guitar class is defined in guitar.py

def main():
    gibson_l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 500)

    # Testing get_age()
    print(f"{gibson_l5.name} get_age() - Expected 100. Got {gibson_l5.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")

    # Testing is_vintage()
    print(f"{gibson_l5.name} is_vintage() - Expected True. Got {gibson_l5.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

   
if __name__ == "__main__":
    main()
