from kivy.uix.widget import Widget
from field.lane import Lane, LANE
from src.levels import LEVEL1_LANE


class Field(Widget):
    """Field Widget"""

    def __init__(self, level, **kwargs):
        super().__init__(**kwargs)
        self.level = level
        self.all_lane_list = list()
        self.all_avail_lane = list()
        self.set_no_lane()
        self.all_lane()

    def set_no_lane(self):
        if self.level == "LEVEL1":
            self.all_no_lane = LEVEL1_LANE

    def all_lane(self):
        for i in range(LANE):
            setattr(self, f"lane{i}", Lane(
                "normal" if i+1 not in self.all_no_lane else "", i))
            self.all_lane_list.append(getattr(self, f"lane{i}"))
            if i+1 not in self.all_no_lane:
                self.all_avail_lane.append(getattr(self, f"lane{i}"))
            self.add_widget(getattr(self, f"lane{i}"))
