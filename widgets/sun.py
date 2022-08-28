from random import randint
from kivy.uix.image import Image
from configuration import FRAME, WIDTH, HEIGHT
from kivy.animation import Animation
from kivy.utils import get_color_from_hex as gc


class Sun(Image):

    def __init__(self, value=25, **kwargs):
        super().__init__(**kwargs)
        self.stop = False
        self.disappear_limit = 30*FRAME
        self.color = gc("#fbff00")
        self.value = value
        self.size = HEIGHT*0.1, HEIGHT*0.1
        self.pos = (randint(WIDTH*0.2, WIDTH-self.width), HEIGHT)
        self.limit = randint(HEIGHT/2, HEIGHT-self.height)

    def update(self):
        if self.stop:
            return False
        elif self.limit <= 0:
            self.disappear_limit -= 1
            self.check_disappear_opacity()
        else:
            self.y -= 1
            self.limit -= 1

    def check_disappear_opacity(self):
        if (self.disappear_limit/(30*FRAME))*100 == 50.0:
            Animation(opacity=0.8, d=0.25, t="linear").start(self)
        elif (self.disappear_limit/(30*FRAME))*100 == 25.0:
            Animation(opacity=0.5, d=0.25, t="linear").start(self)
        elif self.disappear_limit == 0:
            anim = Animation(opacity=0, d=0.25, t="linear")
            anim.start(self)
            anim.bind(on_complete=self.remove)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.stop is False:
                if not self.disappear_limit == 0:
                    self.animate_sun()
        return super().on_touch_down(touch)

    def animate_sun(self):
        self.stop = True
        anim = Animation(pos=self.parent.parent.sunslot.pos,
                         d=0.5, t="linear")
        anim.start(self)
        anim.bind(on_complete=self.remove)

    def remove(self, *_):
        self.parent.parent.sunslot.sun_hold += self.value
        self.parent.remove_widget(self)
