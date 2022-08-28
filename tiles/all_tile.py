from kivy.uix.image import Image
from kivy.utils import get_color_from_hex as gc


class NormalTile(Image):
    def __init__(self, color=0, ranked=0, **kwargs):
        super().__init__(**kwargs)
        self.ranked = ranked
        self.type = "normal"
        self.fighter = None
        self.color = gc("#919191") if color % 2 else gc("#636362")


class NoTile(Image):
    def __init__(self, ranked=0, **kwargs):
        super().__init__(**kwargs)
        self.ranked = ranked
        self.type = "notile"
        self.color = gc("#96600e")
