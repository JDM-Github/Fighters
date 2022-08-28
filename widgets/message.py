from configuration import WIDTH, HEIGHT
from kivy.utils import get_color_from_hex as gc
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.metrics import sp
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.animation import Animation


class MessageBox(Widget):
    """Message Box when something happen"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = WIDTH, sp(64)
        self.pos = 0, HEIGHT*0.1
        self.display_bg()
        self.display_text()
        self.timer = Clock.schedule_once(
            lambda _: self.change_opacity(), 4)

    def change_opacity(self):
        self.opacity = 0

    def display_bg(self):
        self.bg = Image()
        self.bg.color = (0, 0, 0, 1)
        self.bg.opacity = 0.4
        self.bg.size = self.size
        self.bg.pos = self.pos
        self.add_widget(self.bg)

    def display_text(self):
        self.lab = Label(text="")
        self.lab.bold = True
        self.lab.font_name = "rex"
        self.lab.font_size = sp(32)
        self.lab.size = self.size
        self.lab.pos = self.pos
        self.lab.bind(text=self.animate_text)
        self.add_widget(self.lab)

    def animate_text(self, *_):
        anim = Animation(color=gc("#FF0000"), d=0.05, t="linear")
        anim += Animation(color=gc("#FFFFFF"), d=0.1, t="linear")
        anim.start(self.lab)


class Message(MessageBox):
    """Message Box in Middle used in Game Loop"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos = (0, (HEIGHT/2)-(self.height/2))
        self.lab.pos = self.pos
        self.bg.pos = self.pos
        self.lab.color = gc("#FF0000")
        self.lab.unbind(text=self.animate_text)

    def change_opacity(self):
        self.parent.remove_widget(self)
        return super().change_opacity()
