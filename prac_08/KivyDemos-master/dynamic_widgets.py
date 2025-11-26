"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Lindsay Ward, first version: 16/11/2025
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app and set up data (model)."""
        super().__init__(**kwargs)
        # basic data model: list of names
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Alice Amber"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_widgets.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a Label for each name and add it to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
