from unreliable_car import UnreliableCar


def main():
    # Make two cars
    good_car = UnreliableCar("Almost New", 100, 90)   # 90% chance to drive
    bad_car = UnreliableCar("Old Bomb", 100, 30)      # 30% chance to drive

    print("Testing UnreliableCar...")

    # Try to drive each car several times
    for i in range(1, 11):
        print(f"\nAttempt {i}:")
        distance_good = good_car.drive(10)
        distance_bad = bad_car.drive(10)

        print(f"{good_car.name} tried to drive 10km and drove {distance_good}km")
        print(f"{bad_car.name} tried to drive 10km and drove {distance_bad}km")

    print("\nFinal states:")
    print(f"{good_car.name}: fuel = {good_car.fuel}, odometer = {good_car.odometer}")
    print(f"{bad_car.name}: fuel = {bad_car.fuel}, odometer = {bad_car.odometer}")


if __name__ == "__main__":
    main()
