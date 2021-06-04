import  kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=1

        self.inside=GridLayout()
        self.inside.cols=2

        self.inside.add_widget(Label(text="first name"))
        self.name1=TextInput(multiline=False)
        self.inside.add_widget(self.name1)

        self.inside.add_widget(Label(text="first name"))
        self.name2=TextInput(multiline=False)
        self.inside.add_widget(self.name2)

        self.inside.add_widget(Label(text="first name"))
        self.name3=TextInput(multiline=False)
        self.inside.add_widget(self.name3)

        self.add_widget(self.inside)

        self.submit=Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self,instance):
        x=self.name1.text
        y=self.name2.text
        z=self.name3.text
        print(x,y,z)
        # to blank the input box/field
        self.name1.text=''
        self.name2.text=''
        self.name3.text=''

class Firstapp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    Firstapp().run()            
print(":dd")