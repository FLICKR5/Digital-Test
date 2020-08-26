import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2 
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline = False)
        self.add_widget(self.email)

        self.add_widget(Label(text="Passwod: "))
        self.password = TextInput(multiline = False)
        self.add_widget(self.password)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        print(self.name.text)
        print(self.email.text)
        print(self.password.text)
        self.name.text=""
        self.email.text=""
        self.password.text=""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()