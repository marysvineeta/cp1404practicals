from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def taxi_simulation():
    available_taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0.0
    selected_taxi = None

    print("Welcome to the taxi simulator!")
    options_menu = "q)uit, c)hoose taxi, d)rive"

    while True:
        print(options_menu)
        action = input(">>> ").lower()

        if action == "q":
            break
        elif action == "c":
            show_taxis(available_taxis)
            selected_taxi = pick_taxi(available_taxis)
        elif action == "d":
            if selected_taxi is None:
                print("Please choose a taxi before driving.")
            else:
                total_cost += take_trip(selected_taxi)
        else:
            print("Invalid choice. Please select a valid option.")

        print(f"Current bill: ${total_cost:.2f}")

    print(f"Total bill: ${total_cost:.2f}")
    print("Final taxi statuses:")
    show_taxis(available_taxis)

def show_taxis(taxi_list):
    for index, taxi in enumerate(taxi_list):
        print(f"{index} - {taxi}")

def pick_taxi(taxi_list):
    try:
        choice = int(input("Select taxi: "))
        if 0 <= choice < len(taxi_list):
            return taxi_list[choice]
        else:
            print("Invalid taxi selection.")
    except ValueError:
        print("Please enter a valid number.")

def take_trip(taxi):
    distance = float(input("Enter the distance to drive: "))
    taxi.start_fare()
    taxi.drive(distance)
    trip_cost = taxi.get_fare()
    print(f"Your trip with {taxi.name} cost ${trip_cost:.2f}")
    return trip_cost

if __name__ == "__main__":
    taxi_simulation()
