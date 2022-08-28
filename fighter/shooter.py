from configuration import FRAME, WIDTH, HEIGHT, TILE, LANE
from fighter.fighter import Fighter
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex as gc


class Bullet(Image):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (((WIDTH*0.8)/TILE)/2,
                     ((HEIGHT*0.8)/LANE)/2)


class Shooter(Fighter):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.health = 100
        self.sight_range = TILE  # Means all Tile
        self.reload_shot = 5*FRAME
        self.sun_value = 100
        self.damage = 10
        self.color = gc("#99ff99")
        self.old_color = self.color

    def iniate_battle(self):
        self.all_shoot = Widget()
        self.parent.parent.add_widget(self.all_shoot)

    def update(self):
        if self.check_range():
            self.reload_shot -= 1
            if self.reload_shot <= 0:
                self.shoot()
                self.reload_shot = 5*FRAME
        else:
            self.reload_shot = 5*FRAME
        for bull in self.all_shoot.children:
            bull.x += 2
            for enemy in self.parent.parent.all_enemies.children:
                if enemy.collide_point(*bull.pos):
                    enemy.health -= self.damage
                    self.all_shoot.remove_widget(bull)
                    break
            else:
                if bull.x >= WIDTH+bull.width:
                    self.all_shoot.remove_widget(bull)

    def check_range(self):
        for enemy in self.parent.parent.all_enemies.children:
            if self.tile.parent.lane_row == enemy.row_pos.lane_row:
                if enemy.ranked - self.tile.ranked <= self.sight_range and enemy.ranked - self.tile.ranked >= 0:
                    return True
        return False

    def shoot(self):
        bullet = Bullet()
        bullet.center = self.center
        self.all_shoot.add_widget(bullet)
