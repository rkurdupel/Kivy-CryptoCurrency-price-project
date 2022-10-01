from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy import Config
from kivy.uix.image import Image
import os
from count import Count

Config.set('graphics', 'multisamples', '0')
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class ScreenButton(Button):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)  # super() - використовується щоб отримати всі дані з класу який наслідується (Button)

        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction # щоб при натисканні на кнопку була анімація переходу на інший екран (left, right)
        self.screen.manager.current = self.goal # щоб при натисканні на кнопку змінювався екран на інший (який заданий в goal в створенні кнопки)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(font_size = "24sp",size_hint = (1,1), pos_hint = {'center_x': 0.5, 'center_y': 0.9},  text = "Welcome to cryptocurrency project !\n       Pick one of available buttons")   # center_y: 0.9 - вверх екрану по (y), center_x: 0.5 - центр екрану по (x)
        image = Image(source = "picture.png", size_hint = (0.6, 0.6), pos_hint = {"x": 0.2, "y": 0.3})
        
        v1 = BoxLayout(orientation = "vertical")

        button1 = ScreenButton(self, direction = "left", goal = "getcryptoprice", text = "Get price of crypto", size_hint=(0.5, 0.1), pos_hint={'x':0.25, 'y':0.2})      # size_hint - розмір об'єкта, pos_hint - координати об'єкта

        #v1.add_widget(label)
        #v1.add_widget(image)

        self.add_widget(label) # щоб всі об'єкти появились в певному екрані в програмі
        self.add_widget(image)
        self.add_widget(button1)
       

class GetCryptoPrice(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text = "Discover the price of crypto", font_size = "50sp", pos_hint = {"x": 0, "y": 0.4})
        image = Image(source = "list_of_cryptoo.png", size_hint = (1, 0.5), pos_hint = {"x": 0, "y": 0.33})
        label2 = Label(text = "Put down short name of cryptocurrency + USDT (BTCUSDT)", pos_hint = {"x": -0.00001, "y": -0.2})
        self.entry = TextInput(hint_text = "Write info here", multiline = False, size_hint = (0.3, None), pos_hint = {"x": 0.25, "y": 0.23}, height = "30sp", halign = "center")  # halign = "center" - розміщує текст всередині надпису посередині, перше слово починається з центру писатись
        # height - задати висоту рядка, size_hint = (0,5, None) 0.5 - розмір по (x), None - розмір по (y)
        self.result = Label(text = 'Price:', font_size = "24sp", pos_hint = {'x': 0, 'y': -0.3})

        back_button = ScreenButton(self,direction = "right", goal = "main", text = "<-- Back", size_hint = (0.3, 0.1),  pos_hint = {"x": 0.7, "y":0})

        #v1 = BoxLayout(orientation = "vertical")
        #v1.add_widget(label)
        #v1.add_widget(image)
        #v1.add_widget(label2)
        #v1.add_widget(entry)

        self.add_widget(label)
        self.add_widget(image)
        self.add_widget(label2)
        self.add_widget(self.entry) 
        self.add_widget(self.result)
        self.add_widget(back_button)     # Добавити всі об'єкти на екран за допомогою add_widget()

        self.entry.bind(text = self.count)  # bind допомагає задіяти певному об'єкту виконання (при введені інформації в видимий рядок - виконується функція count)

        # self - звернення до певного об'єкту, корисний коли потрібно використати певний об'єкт в різних методах
        # метод - функція всередині класу
        

    def count(self, *args):
        data = self.entry.text.upper()  # upper() - переводе всі букви з маленьких в великі (abc --> ABC)
        #self.result.text = f"Price: {Count(data)}"

        #self.result.text = "Price:"

        

        try:    # коли користувач вводе крипту в якої більше 6 символів в назві щоб ті букви пропускались поки не можна буде вивести ціну
            self.result.text = f"Price: {Count(data, self.result)}"
        except KeyError:
            print(1)
            #self.result.text = "Price:"
            #pass
        else:
            self.result.text = f"Price: {Count(data, self.result)}"

        
    


class MyApp(App):
    def build(self):
        sm = ScreenManager()    # ScreenManager допомагає переключатись між екранами
        sm.add_widget(MainScreen(name = "main"))    # name = "main" - задати назву екрану MainScreen - main, за допомогою **kwargs
        sm.add_widget(GetCryptoPrice(name = "getcryptoprice"))

        return sm   # відобразити екрани (зробити екрани видимими в програмі)

app = MyApp()   # створити об'єкт класу MyApp
app.run()   # запустити програму та відобразити всі об'єкти на екрані
