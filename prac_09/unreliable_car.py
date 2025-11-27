import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of Car that sometimes does not drive as expected."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        # Car fails to drive at all
        return 0
