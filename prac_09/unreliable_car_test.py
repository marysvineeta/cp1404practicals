from unreliable_car import UnreliableCar

def test_unreliable_car():
    """Test the UnreliableCar class by attempting multiple drives."""
    car = UnreliableCar("Faulty Prius", 100, 50)

    for attempt in range(1, 6):
        distance_travelled = car.drive(20)
        print(f"Drive {attempt}: Car traveled {distance_travelled} km. Fuel remaining: {car.fuel}.")

if __name__ == "__main__":
    test_unreliable_car()
