from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex


class MainApp(App):

    def build(self):

        self.buttons = [["7", "8", "9", "/"],
                        ["4", "5", "6", "*"],
                        ["1", "2", "3", "-"],
                        [".", "0", "C", "+"],
                        ["="]
                        ]
        self.operators = ["/", "*", "-", "+"]

        self.azul = '#56DEFF'

        self.solution = TextInput(readonly=True, text='')
        self.main_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        self.main_layout.add_widget(self.solution)
        self.equal_button = Button(text="=", pos_hint={"center_x": .5, "center_y": .5})
        for row in self.buttons:
            r_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": .5, "center_y": .5},
                                background_color=get_color_from_hex(self.azul))

                button.bind(on_press=self.on_button_press)
                r_layout.add_widget(button)
            self.main_layout.add_widget(r_layout)

        return self.main_layout

    def on_button_press(self, instance):
        if instance.text != '=' and instance.text != 'C':
            self.solution.text += instance.text
        elif instance.text == 'C':
            self.solution.text = ''
        else:
            try:
                result = eval(self.solution.text)
                self.solution.text = str(result)
                print(result)
            except SyntaxError:
                print("Invalid syntax in expression")


if __name__ == '__main__':
    app = MainApp()
    app.run()
