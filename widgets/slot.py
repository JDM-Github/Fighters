from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.factory import Factory
from all_flag import Flag
from flag import Rules
from widgets.message import MessageBox


class Slot(Image):

    def __init__(self, type_slot, **kwargs):
        super().__init__(**kwargs)
        self.type_slot = type_slot
        self.slot_hold = list()
        self.grab_x = None
        self.grab_y = None
        self.get_plants()

    def get_plants(self):
        if self.type_slot == "shooter":
            self.slot_hold.append(Factory.Shooter())
            self.slot_hold[-1].opacity = 0.5

    def set_position(self):
        self.slot_hold[-1].pos = self.pos

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.grab_x = self.x - touch.x
            self.grab_y = self.y - touch.y
            self.set_position()
            self.parent.parent.all_fighter.add_widget(self.slot_hold[-1])
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.slot_hold[-1].pos = (touch.x + self.grab_x,
                                      touch.y + self.grab_y)
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            if not self.check_if_avail(touch.pos):
                self.slot_hold[-1].pos = self.pos
                self.parent.parent.all_fighter.remove_widget(
                    self.slot_hold[-1])
        return super().on_touch_up(touch)

    def check_if_avail(self, pos):
        for lane in self.parent.parent.field.all_lane_list:
            for lane_chil in lane.children:
                if lane_chil.collide_point(*pos):
                    if lane_chil.type == "notile":
                        if Flag.FLAG_RULE_01 is False:
                            self.add_message("camp_on_notile")
                        return False
                    elif lane_chil.fighter is not None or self.check_if_enough_sun() is False:
                        return False
                    self.parent.parent.sunslot.sun_hold -= \
                        self.slot_hold[-1].sun_value
                    lane_chil.fighter = self.slot_hold[-1]
                    self.slot_hold[-1].iniate_battle()
                    self.slot_hold[-1].opacity = 1
                    self.slot_hold[-1].tile = lane_chil
                    self.slot_hold[-1].pos = lane_chil.pos
                    self.get_plants()
                    return True
        return False

    def check_if_enough_sun(self):
        if not (self.parent.parent.sunslot.sun_hold - self.slot_hold[-1].sun_value) >= 0:
            if Flag.FLAG_RULE_02 is False:
                self.add_message("not_enough_energy")
            return False
        return True

    def add_message(self, rule):
        if self.parent.parent.rule_obj is not None:
            self.parent.parent.remove_widget(self.parent.parent.rule_obj)
            self.parent.parent.rule_obj.timer.cancel()
            self.parent.parent.rule_obj = None
        self.parent.parent.rule_obj = Rules(rule)
        self.parent.parent.add_widget(self.parent.parent.rule_obj)
