from kivymd.app import MDApp as App
from kivymd.uix.button import MDRoundFlatButton as Button
from kivymd.uix.label import MDLabel as Label
from kivymd.uix.boxlayout import MDBoxLayout as BoxLayout
from kivymd.uix.screenmanager import MDScreenManager as ScreenManager 
from kivymd.uix.screen import MDScreen as Screen
#from kivymd.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextField as TextInput
from kivymd.uix.button import MDFillRoundFlatButton
from kivy import Config
#from kivymd.uix.behaviors.backgroundcolor
#from kivy.core.window import Window
#from kivymd.uix.image import MDImage as Image

from kivymd.uix.navigationrail import MDNavigationRail, MDNavigationRailItem

from kivy.uix.popup import Popup # з kivy.uix.popup імпортувати клас Popup, вікно яке часто використовується щоб на екрані показати помилку як окреме вікно


import os
from count import Count
from count import cryptoget


from kivy.lang import Builder
from kivymd.uix.fitimage import FitImage as Image

#window.Window.clearcolor = (.9, .9, .9, 1)
#Window.clearcolor = (4, 4, 5, 5)

Config.set('graphics', 'multisamples', '0')
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

#class MoveToAnotherScreen(Button):
#    def __init__(self,name, **kwargs):
#        super().__init__(**kwargs)
    

#    def change_on_capybara_screen(self):
          #screen.manager.current = CapybaraScreen
#moveto = MoveToAnotherScreen(name = "movetoanotherscreen")  # зробити екземпляр класу MoveToAnotherScreen

class CapybaraScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # отримати конструктор з класа батька (Screen)


        popup = Popup(title = "title", content = Label(text = "Text"), size_hint = (0.1, 0.1))  # зробити видиме вікно маленьке (для прикладу щоб друкувати помилки (Error))
        # title - заголовок вікна, 
        # content - текст який всередині вікна
        #  button = Button(text = "press")
        
        #popup.bind(on_dismiss = function)  # при закритті вікна (popup) яке появиться виконається певна дія  (наприклад: програма  закінчить роботу), за допомогою on_dismiss (на відміну, при відміні) 
        
        popup.open()    # відкрити маленьке вікно (popup)

        #capyone = Button(text = "Start <| ", on_press = "capybara.gif")
        capyone = Image(source = "capy.jpg")

        cryptopage = MDNavigationRailItem(text = "Crypto", icon = "currency-usd", on_press = app.change_on_crypto_screen)
        capybarapage = MDNavigationRailItem(text = "Capybara's", icon = "camera-wireless-outline", on_press = app.change_on_capybara_screen)
        # MoveToAnotherScreen.change_on_capybara_screen

        navigation = MDNavigationRail(cryptopage, capybarapage)                  # за допомогою MDNavigationRail, MDNavigationRailItem зробити можливість переключатись між екранами
        self.add_widget(capyone)
        self.add_widget(navigation)

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

        label = Label(font_size = "24sp",size_hint = (1,1), pos_hint = {'center_x': 0.5, 'center_y': 0.9},  text = "Welcome to cryptocurrency project !\n       Pick one of available buttons", font_style = "H1", halign = "center")   # center_y: 0.9 - вверх екрану по (y), center_x: 0.5 - центр екрану по (x)
        # halign = "center" - вирівняти текст по центру екрану
        # font_style - тип шрифта
        image = Image(source ="picture.png", size_hint = (0.6, 0.6), pos_hint = {"x": 0.2, "y": 0.25})
        # Builder.load_string

        v1 = BoxLayout(orientation = "vertical")

        button1 = ScreenButton(self, direction = "left", goal = "getcryptoprice", text = "Get price of crypto", size_hint=(0.5, 0.1), pos_hint={'x':0.25, 'y':0.15})      # size_hint - розмір об'єкта, pos_hint - координати об'єкта
        button2 = ScreenButton(self, direction = "left", goal = "convert", text = "Converter", size_hint = (0.5, 0.1), pos_hint = {'x': 0.25, 'y': 0.03})

        self.select_theme = MDFillRoundFlatButton(text = "Select theme of application", size_hint = (0.2, 0.1), pos_hint = {"x": 0, "y": 0}, on_release = app.change_style) 
        # app.change_style - функція, app - об'єкт класу MyApp, change_style - метод (метод - функція всередині класу) всередині класу MyApp 
        # on_release - дія яка буде виконуватись при натиснанні на кнопку, функція має бути без () інакше вона зразу виконається та надрукується помилка що результат None

        #v1.add_widget(label)
        #v1.add_widget(image)

        cryptopage = MDNavigationRailItem(text = "Crypto", icon = "currency-usd", on_press = app.change_on_crypto_screen)
        capybarapage = MDNavigationRailItem(text = "Capybara's", icon = "camera-wireless-outline", on_press = app.change_on_capybara_screen)
        # MoveToAnotherScreen.change_on_capybara_screen

        navigation = MDNavigationRail(cryptopage, capybarapage)                  # за допомогою MDNavigationRail, MDNavigationRailItem зробити можливість переключатись між екранами
        #type = "unselected"

        #if cryptopage.style == "Selected":
            #print(1)
        #capypage = MDNavigationRail())


        self.add_widget(label) # щоб всі об'єкти появились в певному екрані в програмі
        self.add_widget(image)
        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(self.select_theme)
        self.add_widget(navigation)
        #self.add_widget(capypage)

    def test(self, *args):
        print("hello")
    


       
# ОБ'ЄКТИ LABEL РОЗМІЩАЮТЬСЯ ПРИ СТВОРЕННІ ПО ЦЕНТРУ, ОБ'ЄКТИ TextInput, ScreenButton, Button З ЛІВОГО НИЖНЬОГО КУТА
class ConvertScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text = "USD convert to cryptocurrency", font_size = "45sp", pos_hint = {"x": -0.1, "y": 0.4}, font_style = "H1")
        convert_image = Image(source = "convert_logo.png", size_hint = (0.4, 0.2), pos_hint = {"x": 0.7, "y":  0.8})  # source - використовується щоб задавати картинку для використання в програмі
        # 0.8 - вверх екрану, 0.7 - правий кут екрану, -0.3 (З центру) - лівий кут екрану

        usd = Label(text = "How many USD do you have?", font_size = "23sp", pos_hint = {"x": 0, "y": 0.1}, font_style = "Body1")

        self.usd_sum = TextInput(hint_text = "Write the amount of USD which you have", multiline = False, size_hint = (0.4, 0.1), height = 30, pos_hint = {"x": 0, "y": 0.45})

        crypto_ask = Label(text = "Which cryptocurrency do you want? Write name of cryptocurrency + USDT (ETHUSDT)", font_size = "15sp", pos_hint = {"x": 0, "y": -0.09}, font_style = "Body2")

        self.crypto_entry = TextInput(hint_text = "Put down the name of the cryptocurrency you want", size_hint = (0.4, 0.1), height = 30, pos_hint = {"x": 0, "y": 0.3})

        self.you_can_get = Label(text = "You can buy:", font_size = "30sp", pos_hint = {"y": -0.35, "x": 0.3}, font_style = "Subtitle1")
        # TextInput - пустий видимий рядок в якому можна писати

        back_button = ScreenButton(self, direction = "right", goal = "main", text = "<--- Back",size_hint = (0.3, 0.1), pos_hint = {"x": 0.7, "y": 0.28})
        refresh_button = Button(text="Refresh data", size_hint=(0.3, 0.1), pos_hint={"x": 0.7, "y": 0.5})

        self.add_widget(label)
        self.add_widget(convert_image)
        self.add_widget(usd)
        self.add_widget(self.usd_sum)
        self.add_widget(crypto_ask)
        self.add_widget(self.crypto_entry)
        self.add_widget(self.you_can_get)
        self.add_widget(back_button)
        self.add_widget(refresh_button)     # Добавити всі об'єкти на екран за допомогою add_widget()

        refresh_button.bind(on_press=self.refresh)

        self.crypto_entry.bind(text = self.how_many_can_you_buy)

    def refresh(self, *args):
        try:        # спробувати очистити дані в видимому рядку
            self.usd_sum.text = ""
            self.crypto_entry.text = "" # crypto_entry.text має бути на першому місці бо в usd_sum виконується змінювання типу з string (str) в float
        except ValueError: # при помилці ValueEror (помилка значення) надрукувати 76
            print(76)   # надрукувати 76


    def how_many_can_you_buy(self, *args):  # *args - приймає безліч неіменованих аргументів (5, "grghr", 64645") та повертає в вигляді кортежу ()
        get_usd = float(self.usd_sum.text)  # перевести дані які користувач ввів в рядку з string в float (число з крапкою)
        data = self.crypto_entry.text.upper()   # upper() - переводе всі букви з маленьких в великі (pow -> POW)

        try:
            self.you_can_get.text = f"You can buy: {cryptoget(cryptoname = data, usd = get_usd)}"
        except KeyError:
            print(9549459)

# ОБ'ЄКТИ LABEL РОЗМІЩАЮТЬСЯ ПРИ СТВОРЕННІ ПО ЦЕНТРУ, ОБ'ЄКТИ TextInput, ScreenButton, Button З ЛІВОГО НИЖНЬОГО КУТА
class GetCryptoPrice(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text = "Discover the price of crypto", font_size = "50sp", pos_hint = {"x": 0, "y": 0.4}, font_style = "H1")
        image = Image(source = "list_of_cryptoo.png", size_hint = (1, 0.5), pos_hint = {"x": 0, "y": 0.33})
        label2 = Label(text = "Put down short name of cryptocurrency + USDT (BTCUSDT)", pos_hint = {"x": 0, "y": -0.2}, font_style = "Subtitle1")
        self.entry = TextInput(hint_text = "Write info here", multiline = False, size_hint = (0.3, None), pos_hint = {"x": 0, "y": 0.23}, height = "30sp", halign = "center")  # halign = "center" - розміщує текст всередині надпису посередині, перше слово починається з центру писатись
        # height - задати висоту рядка, size_hint = (0,5, None) 0.5 - розмір по (x), None - розмір по (y)
        # None - 0 може бути розмір або координати певного об'єкта
        # multiline = False - щоб вся введена користувачем інформацію в видимому рядку була в один рядок

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

        #window.Window.clearcolor = (.9, .9, .9, 1)
        #window.Window.backgroundcolor = "FFFFCC"
        #window.Window.clearcolor = (0, 0, 0, 1)

        self.theme_cls.theme_style = "Dark" # тема додатку (Dark - темна, Light - світла, всі назви з великої букви)
        self.theme_cls.primary_palette = "Blue"   # колір об'єктів інтерфейсу    # звчиайний колір - світло синій  (bright blue)
        self.theme_cls.primary_hue = "A400"  # відтінок
        self.theme_cls.accent_palette = "Red"

        self.sm = ScreenManager()    # ScreenManager допомагає переключатись між екранами
        self.sm.add_widget(MainScreen(name = "main"))    # name = "main" - задати назву екрану MainScreen - main, за допомогою **kwargs
        self.sm.add_widget(GetCryptoPrice(name = "getcryptoprice"))
        self.sm.add_widget(ConvertScreen(name = "convert"))
        self.sm.add_widget(CapybaraScreen(name = "capy"))

        return self.sm   # відобразити екрани (зробити екрани видимими в програмі)
    
    def change_style(self, *args):  # функція для зміну теми програми
        if self.theme_cls.theme_style == "Dark":    # якщо тема програми чорна - змінити тему на світлу, та задати колір об'єктам жовтий
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Yellow"

        elif self.theme_cls.theme_style == "Light": # якщо тема програми світла - змінити на чорну, задати колір об'єктам синій та задати відтінок
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Blue"
            self.theme_cls.primary_hue = "A400"

    def change_on_capybara_screen(self, *args):
        self.sm.current = "capy"
        #self.sm.switch_to(screen = "capy")
    def change_on_crypto_screen(self, *args):   # * args забирає помилку з двома аргументами, при натисненні на кнопку створюється неіменований аргумент який потрапляє в *args
        self.sm.current = "main"




app = MyApp()   # створити об'єкт класу MyApp
app.run()   # запустити програму та відобразити всі об'єкти на екрані


# ОБ'ЄКТИ LABEL РОЗМІЩАЮТЬСЯ ПРИ СТВОРЕННІ ПО ЦЕНТРУ, ОБ'ЄКТИ TextInput, ScreenButton, Button З ЛІВОГО НИЖНЬОГО КУТА
