from configuration import SLOT_AVAIL, WIDTH, HEIGHT
from widgets import Slot
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp


class SlotHolder(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spacing = dp(5)
        self.slot_height = HEIGHT*0.1
        self.slot_width = self.slot_height-((WIDTH-HEIGHT)*0.05)
        self.rows = 1
        self.cols = SLOT_AVAIL
        self.size = (self.slot_width*SLOT_AVAIL, self.slot_height)
        self.pos = (WIDTH*0.2, HEIGHT-self.slot_height)
        self.display_slot()

    def display_slot(self):
        for i in range(SLOT_AVAIL):
            setattr(self, f"slot{i}", Slot("shooter"))
            self.add_widget(getattr(self, f"slot{i}"))
