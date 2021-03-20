from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import *
from kivy.uix.switch import Switch
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.list import *
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivymd.app import MDApp

key = {
    "A": "G", "B": "K", "C": "D", "D": "P", "E": "S", "F": "W", "G": "Y", "H": "X", "I": "F", "J": "B", "K": "A",
    "L": "I", "M": "C", "N": "M", "O": "N", "P": "Q", "Q": "E", "R": "Z", "S": "U", "T": "J", "U": "H", "V": "R",
    "W": "O", "X": "V", "Y": "L", "Z": "T"
}

#msg = input("Input the message you want to code: ")
#inp = input("Input message to be decoded here: ")
key_list = list(key.keys())
val_list = list(key.values())
encoded = []
decoded = []

Window.size = (300, 500)

KV = """
MDNavigationLayout:
    MDToolbar:
        title: " "
        MDIconButton:
            icon: "arrow-right"
            pos_hint: {"center_x": .5, "center_y": .5}
            theme_text_color: "Custom"
            text_color: "white"
            on_release:
                screen_manager.current = "Decoder"
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .5, "center_y": .5}
            theme_text_color: "Custom"
            text_color: "white"
            on_release:
                screen_manager.current = "Encoder"
    ScreenManager:
        id: screen_manager
        Screen:
            name: "Encoder"
            id: "Encoder"
            MDTextField:
                id: "enc"
                hint_text: "ENCODE"
                helper_text: "Type the message you want to ENCODE here"
                helper_text_mode: "on_focus"
                pos_hint: {"center_y": .5}
                on_text_validate:
                    app.show_alert_dialog_encoded(self)

        Screen:
            name: "Decoder"
            id: "Decoder"
            MDTextField:
                id: "dec"
                hint_text: "DECODE"
                helper_text: "Type the message you want to DECODE here"
                helper_text_mode: "on_focus"
                pos_hint: {"center_y": .5}
                on_text_validate:
                    app.show_alert_dialog_decoded(self)
"""


class MainApp(MDApp):
    dialog = None
    encoded = []
    decoded = []

    def __init__(self, **kwargs):
        self.title = "APP"
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog_encoded(self, enc):
        self.textfield = enc
        self.encode(enc)
        self.join()
        if not self.dialog:
            self.dialog = MDDialog(
                title="Your encoded message",
                text=self.joined,
                buttons=[
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def show_alert_dialog_decoded(self, dec):
        self.textfield = dec
        self.decode(dec)
        self.join2()
        if not self.dialog:
            self.dialog = MDDialog(
                title="Your decoded message",
                text=self.joined2,
                buttons=[
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        self.textfield.text = ""
        self.encoded = []
        self.decoded = []
        self.dialog = None

    def encode(self, enc):
        for letter in enc.text:
            if letter == " ":
                letter = " "
                self.encoded.append(letter)
            else:
                letter = letter.upper()
                letter = key[letter]
                self.encoded.append(letter)

    def decode(self, dec):
        for char in dec.text:
            if char == " ":
                char = " "
                self.decoded.append(char)
            else:
                char = char.upper()
                position = val_list.index(char)
                self.decoded.append(key_list[position])

    def join(self):
        self.joined = ''.join(self.encoded)
        return self.joined

    def join2(self):
        self.joined2 = ''.join(self.decoded)
        return self.joined2


app = MainApp()
app.run()
