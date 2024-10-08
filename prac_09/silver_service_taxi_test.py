from silver_service_taxi import SilverServiceTaxi

from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    luxury_taxi = SilverServiceTaxi("Fancy Limo", 100, 2)

    # Drive the taxi for 18 km
    luxury_taxi.drive(18)

    fare = luxury_taxi.get_fare()
    print(f"Expected rounded fare: $48.80, Calculated fare: ${fare:.2f}")
    assert fare == 48.80, f"Test failed: expected fare $48.80, got ${fare:.2f}"

    # Print the details
    print(luxury_taxi)

if __name__ == "__main__":
    test_silver_service_taxi()
