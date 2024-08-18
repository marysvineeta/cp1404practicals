import random
from prac_09.car import Car

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        # Generate a random number between 0 and 100
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            actual_distance = super().drive(distance)
        else:
            actual_distance = 0
        return actual_distance
