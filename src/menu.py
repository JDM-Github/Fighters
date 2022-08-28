from configuration import WIDTH, HEIGHT
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp, sp
from kivy.uix.button import Button


class ButtonClass(Button):

    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = str(text)
        self.font_size = sp(32)
        self.border = [0, 0, 0, 0]
        self.background_color = (0.5, 0.4, 1, 1)


class MenuScreen(Widget):
    """Menu Screen, AKA Starting before playing the game"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_grid()
        self.display_buttons()

    def create_grid(self):
        self.grid = GridLayout()
        self.grid.cols = 1
        self.grid.rows = 3
        self.grid.spacing = dp(20)
        self.grid.size = (WIDTH/2, HEIGHT*0.8)
        self.grid.pos = (WIDTH/2)-(self.grid.width/2), HEIGHT*0.1
        self.add_widget(self.grid)

    def display_buttons(self):
        self.play = ButtonClass("Play")
        self.grid.add_widget(self.play)
        self.grid.add_widget(ButtonClass("Option"))
        self.grid.add_widget(ButtonClass("Exit"))
