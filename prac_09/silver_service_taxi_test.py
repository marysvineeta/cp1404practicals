from silver_service_taxi import SilverServiceTaxi


def main():
    # Basic test with a Hummer
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    hummer.drive(18)
    print(hummer)
    print(f"Fare for Hummer: ${hummer.get_fare():.2f}")

    test_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    test_taxi.drive(18)
    fare = test_taxi.get_fare()
    print(f"Test Taxi fare for 18km: ${fare:.2f}")
    assert abs(fare - 48.80) < 0.01, "Fare should be $48.80"


if __name__ == "__main__":
    main()
