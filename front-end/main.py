import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
#test commit
class MyGrid(Widget):
    question = ObjectProperty(None)
    opt1 = ObjectProperty(None)
    opt2 = ObjectProperty(None)
    opt3 = ObjectProperty(None)
    opt4 = ObjectProperty(None)

    def pressed(self):
        print(self.question.text)
        print(self.opt1.text)
        print(self.opt2.text)
        print(self.opt3.text)
        print(self.opt4.text)

        self.question.text=""
        self.opt1.text=""
        self.opt2.text=""
        self.opt3.text=""
        self.opt4.text=""

        
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
