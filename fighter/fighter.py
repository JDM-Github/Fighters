from kivy.uix.image import Image
from configuration import LANE, TILE, WIDTH, HEIGHT
from kivy.animation import Animation
from kivy.utils import get_color_from_hex as gc
from kivy.properties import NumericProperty


class Fighter(Image):

    health = NumericProperty(100)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tile = None
        self.size = ((WIDTH*0.8)/TILE,
                     ((HEIGHT*0.8)/LANE))
        self.old_color = self.color
        self.bind(health=self.check_health)

    def check_health(self, *_):
        self.fighter_hurt_animation()
        if self.health <= 0:
            self.tile.fighter = None
            self.parent.remove_widget(self)

    def fighter_hurt_animation(self):
        anim = Animation(color=gc("#FFFF99"), d=0.05, t="linear")
        anim += Animation(color=self.old_color, d=0.1, t="linear")
        anim.start(self)
