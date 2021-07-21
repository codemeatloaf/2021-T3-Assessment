# KIVY PRACTICE
# Imports
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

# Define Class

class MyGrid(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyGrid()

# Main Loop
if __name__ == "__main__":
    MyApp().run()
