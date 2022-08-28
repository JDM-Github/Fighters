from random import choice
from configuration import WIDTH, HEIGHT, TILE, LANE, FRAME
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.utils import get_color_from_hex as gc
from kivy.properties import NumericProperty


class NormalEnemy(Image):
    health = NumericProperty(120)
    damage = NumericProperty(30)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attack_cooldown = 3*FRAME
        self.row_pos = 100
        self.color = gc("#333333")
        self.old_color = self.color
        self.size = ((WIDTH*0.8)/TILE,
                     ((HEIGHT*0.8)/LANE))
        self.ranked = 100
        self.bind(health=self.check_health)

    def check_health(self, *_):
        self.enemy_hurt_animation()
        if self.health <= 0:
            if self.parent.parent.enemy_number <= 2:
                self.parent.parent.enemies_first_three_spawn -= 60*FRAME
            else:
                self.parent.parent.enemies_first_three_spawn -= 30*FRAME
            try:
                if self in self.parent.parent.enemy_in_wave:
                    self.parent.parent.enemy_in_wave.remove(self)
                else:
                    self.parent.parent.level_progress.add_progress()
            except TypeError:
                self.parent.parent.level_progress.add_progress()
            self.parent.remove_widget(self)

    def enemy_hurt_animation(self):
        anim = Animation(color=gc("#FF3333"), d=0.05, t="linear")
        anim += Animation(color=self.old_color, d=0.1, t="linear")
        anim.start(self)

    def update(self):
        for fighter in self.parent.parent.all_fighter.children:
            if fighter.collide_point(self.x+(self.width/8), self.y):
                self.enemy_attack(fighter)
                break
        else:
            self.x -= 0.06

    def enemy_attack(self, fighter):
        self.attack_cooldown -= 1
        if self.attack_cooldown <= 0:
            fighter.health -= self.damage
            self.attack_cooldown = 3*FRAME

    def set_position(self):
        self.row_pos = choice(self.parent.parent.field.all_avail_lane)
        self.pos = (WIDTH-1, self.row_pos.y)
        self.bind(pos=self.check_ranked)

    def check_ranked(self, *_):
        for lane in self.row_pos.children:
            if lane.collide_point(*self.pos):
                self.ranked = lane.ranked
                return True
