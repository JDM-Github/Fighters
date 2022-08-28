from configuration import WIDTH, HEIGHT
from factory import Factory
from kivy.app import App
from kivy.core.window import Window
from src import MenuScreen, FightersGame
from kivy.config import Config
from kivy.core.text import LabelBase

Config.set("graphics", "resizable", False)
LabelBase.register("rex", fn_regular="assets/font/Rex-Light.ttf",
                   fn_bold="assets/font/Rex-Bold.ttf")
Window.size = (WIDTH, HEIGHT)


class FightersApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Fighters Game"

    def build(self):
        self.sm = Factory.ScreenManager()
        self.menu = Factory.Screen(name="menu")
        self.menu_screen = MenuScreen()
        self.menu_screen.play.bind(on_release=self.start_game)
        self.menu.add_widget(self.menu_screen)
        self.game = Factory.Screen(name="fighter")
        self.fighter_game = FightersGame()
        self.game.add_widget(self.fighter_game)

        self.sm.add_widget(self.menu)
        self.sm.add_widget(self.game)
        return self.sm

    def start_game(self, *_):
        """Start Game"""
        self.sm.current = "fighter"
        self.fighter_game.start()


if __name__ == "__main__":
    FightersApp().run()
