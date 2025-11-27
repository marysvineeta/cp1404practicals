from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator program."""
    print("Let's drive!")

    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    bill_to_date = 0.0
    current_taxi = None

    choice = ""
    while choice != "Q":
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").strip().upper()

        if choice == "C":
            current_taxi = choose_taxi(taxis)
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date += drive_taxi(current_taxi)
        elif choice == "Q":
            break
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Print the list of taxis"""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Let the user choose a taxi and return it"""
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        chosen_taxi = taxis[taxi_choice]
        return chosen_taxi
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def drive_taxi(current_taxi):
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0

    current_taxi.start_fare()
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    return trip_cost


if __name__ == "__main__":
    main()
