"""
Module for the Project class.
Estimated time: 2 hours
"""

from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def update_completion(self, completion_percentage):
        self.completion_percentage = completion_percentage

    def update_priority(self, priority):
        self.priority = priority
