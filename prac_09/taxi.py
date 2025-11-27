from prac_09.car import Car


class Taxi(Car):

    price_per_km = 1.23  # class variable shared by all Taxis

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")

    def get_fare(self):
        fare = self.price_per_km * self.current_fare_distance
        return round(fare, 1)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
