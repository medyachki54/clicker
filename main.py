from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class ClickerLayout(BoxLayout):
    balance = NumericProperty(265)
    click_power = NumericProperty(3)
    auto_click = NumericProperty(1)

    def on_click(self):
        self.balance += self.click_power

class ClickerApp(App):
    def build(self):
        return ClickerLayout()

if __name__ == '__main__':
    ClickerApp().run()
