from kivy.app import App
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        return Button(text="Calculator")

CalculatorApp().run()
