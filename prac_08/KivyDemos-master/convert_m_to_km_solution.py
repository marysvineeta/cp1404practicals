"""
CP1404/CP5632 Practical
GUI program to convert miles to kilometres.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """App to cnvert miles to kilometres."""
    output_km = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_m_km_solution.kv")
        return self.root

    def handle_calculate(self, text):
        """to convert text to km and update the label."""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)
        # Changing the text triggers on_text→handle_calculate

    def update_result(self, miles):
        """Update output_km """
        self.output_km = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """text to float or return 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
