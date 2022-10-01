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
from count import cryptoget

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

# ОБ'ЄКТИ LABEL РОЗМІЩАЮТЬСЯ ПРИ СТВОРЕННІ ПО ЦЕНТРУ, TextInput, ScreenButton, Button З ЛІВОГО НИЖНЬОГО КУТА
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(font_size = "24sp",size_hint = (1,1), pos_hint = {'center_x': 0.5, 'center_y': 0.9},  text = "Welcome to cryptocurrency project !\n       Pick one of available buttons")   # center_y: 0.9 - вверх екрану по (y), center_x: 0.5 - центр екрану по (x)
        image = Image(source = "picture.png", size_hint = (0.6, 0.6), pos_hint = {"x": 0.2, "y": 0.3})
        
        v1 = BoxLayout(orientation = "vertical")

        button1 = ScreenButton(self, direction = "left", goal = "getcryptoprice", text = "Get price of crypto", size_hint=(0.5, 0.1), pos_hint={'x':0.25, 'y':0.2})      # size_hint - розмір об'єкта, pos_hint - координати об'єкта
        button2 = ScreenButton(self, direction = "left", goal = "convert", text = "Converter", size_hint = (0.5, 0.1), pos_hint = {'x': 0.25, 'y': 0.1})


        #v1.add_widget(label)
        #v1.add_widget(image)

        self.add_widget(label) # щоб всі об'єкти появились в певному екрані в програмі
        self.add_widget(image)
        self.add_widget(button1)
        self.add_widget(button2)
       
# ОБ'ЄКТИ LABEL РОЗМІЩАЮТЬСЯ ПРИ СТВОРЕННІ ПО ЦЕНТРУ, ОБ'ЄКТИ TextInput, ScreenButton, Button З ЛІВОГО НИЖНЬОГО КУТА
class ConvertScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text = "USD convert to cryptocurrency", font_size = "45sp", pos_hint = {"x": -0.1, "y": 0.4})
        convert_image = Image(source = "convert_logo.png", size_hint = (0.4, 0.2), pos_hint = {"x": 0.7, "y":  0.8})  # source - використовується щоб задавати картинку для використання в програмі
        # 0.8 - вверх екрану, 0.7 - правий кут екрану, -0.3 (З центру) - лівий кут екрану

        usd = Label(text = "How many USD do you have?", font_size = "23sp", pos_hint = {"x": -0.3, "y": 0.1})

        self.usd_sum = TextInput(hint_text = "Write the amount of USD which you have", multiline = False, size_hint = (0.4, None), height = 30, pos_hint = {"x": 0, "y": 0.5})

        crypto_ask = Label(text = "Which cryptocurrency do you want? Write name of cryptocurrency + USDT (ETHUSDT)", font_size = "15sp", pos_hint = {"x": -0.13, "y": -0.09})

        self.crypto_entry = TextInput(hint_text = "Put down the name of the cryptocurrency you want", multiline = False, size_hint = (0.45, None), height = 30, pos_hint = {"x": 0, "y": 0.3})

        self.you_can_get = Label(text = "You can buy:", font_size = "30sp", pos_hint = {"y": -0.4, "x": -0.1})
        # TextInput - пустий видимий рядок в якому можна писати

        back_button = ScreenButton(self, direction = "right", goal = "main", text = "<--- Back",size_hint = (0.3, 0.1), pos_hint = {"x": 0.7, "y": 0.28})

        self.add_widget(label)
        self.add_widget(convert_image)
        self.add_widget(usd)
        self.add_widget(self.usd_sum)
        self.add_widget(crypto_ask)
        self.add_widget(self.crypto_entry)
        self.add_widget(self.you_can_get)
        self.add_widget(back_button)

        self.crypto_entry.bind(text = self.how_many_can_you_buy)

    def how_many_can_you_buy(self, *args):  # *args - приймає безліч неіменованих аргументів (5, "grghr", 64645") та повертає в вигляді кортежу ()
        get_usd = float(self.usd_sum.text)
        data = self.crypto_entry.text.upper()   # upper() - переводе всі букви з маленьких в великі (pow -> POW)

        try:
            self.you_can_get.text = f"You can buy: {cryptoget(cryptoname = data, usd = get_usd)}"

        except KeyError:
            print(9549459)

        #print(type(get_crypto))

       # get_crypto = print(cryptoget(self.crypto_entry.text))
       # print(type(get_crypto))
       # count = get_usd * get_crypto
       # print(count)
       # self.you_can_get.text = f"You can buy:{count} {self.crypto_entry.text}"
       # print(34454534)



# ОБ'ЄКТИ LABEL РОЗМІЩАЮТЬСЯ ПРИ СТВОРЕННІ ПО ЦЕНТРУ, ОБ'ЄКТИ TextInput, ScreenButton, Button З ЛІВОГО НИЖНЬОГО КУТА
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
            self.result.text = f"Price: {Count(data)}"
        except KeyError:
            print(1)
            #self.result.text = "Price:"
            #pass
        else:
            self.result.text = f"Price: {Count(data)}"

        
    


class MyApp(App):
    def build(self):
        sm = ScreenManager()    # ScreenManager допомагає переключатись між екранами
        sm.add_widget(MainScreen(name = "main"))    # name = "main" - задати назву екрану MainScreen - main, за допомогою **kwargs
        sm.add_widget(GetCryptoPrice(name = "getcryptoprice"))
        sm.add_widget(ConvertScreen(name = "convert"))

        return sm   # відобразити екрани (зробити екрани видимими в програмі)

app = MyApp()   # створити об'єкт класу MyApp
app.run()   # запустити програму та відобразити всі об'єкти на екрані


# ОБ'ЄКТИ LABEL РОЗМІЩАЮТЬСЯ ПРИ СТВОРЕННІ ПО ЦЕНТРУ, ОБ'ЄКТИ TextInput, ScreenButton, Button З ЛІВОГО НИЖНЬОГО КУТА
