import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MattGrid(Widget):
    pass


class MattApp(App):
    def build(self):
        return MattGrid()

if __name__ == "__main__":
    MattApp().run()