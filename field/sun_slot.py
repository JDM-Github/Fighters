from configuration import WIDTH, HEIGHT
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.metrics import dp


class SunSlot(Image):
    sun_hold = NumericProperty(0)

    def __init__(self, sun_val=100, **kwargs):
        super().__init__(**kwargs)
        self.sun_hold = sun_val
        self.color = (0.6, 0.5, 0, 1)
        self.size = HEIGHT*0.1, HEIGHT*0.1
        self.pos = ((WIDTH*0.2)-self.width)-dp(5), HEIGHT-self.height
        self.display_sun()
        self.bind(sun_hold=self.update_sun)

    def update_sun(self, *_):
        self.lab.text = f"{self.sun_hold}"

    def display_sun(self):
        self.lab = Label(text=f"{self.sun_hold}")
        self.lab.bold = True
        self.lab.font_name = "rex"
        self.lab.size = self.size
        self.lab.pos = self.pos
        self.add_widget(self.lab)
