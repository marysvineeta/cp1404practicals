
from taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)

    # drive 40 km
    my_taxi.drive(40)

    # print taxi details and fare so far
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # start a new fare and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # print taxi details and updated fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
