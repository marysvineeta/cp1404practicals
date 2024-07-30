class Guitar:
    def __init__(self, name="", year=0, cost=0):

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):

        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):

        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage , False otherwise."""
        return self.get_age() >= 50



if __name__ == "__main__":
    gibson_l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(gibson_l5)
    print(f"In {2022}, the {gibson_l5.name} is {gibson_l5.get_age()} years old.")
    print(f"Is the {gibson_l5.name} vintage? {gibson_l5.is_vintage()}")
