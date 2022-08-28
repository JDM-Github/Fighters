from random import choice, randint
from configuration import FRAME, LEVEL_ENERGY_VALUE, LEVEL_ALL_ENERGY
from kivy.metrics import sp
from kivy.utils import get_color_from_hex as gc
from kivy.uix.widget import Widget
from enemies import NormalEnemy
from field import Field, SlotHolder, SunSlot
from kivy.clock import Clock
from src.levels import LEVEL_SCRIPT, LEVEL_SCRIPT_CHOICE, ALL_ENEMY_TYPE
from src.levels import LEVEL1, LEVEL1_TRIGGER, LEVEL1_FINAL_WAVE

from widgets import Sun, Message, LevelProgress


class FightersGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_variable()
        self.all_widget()
        # self.start()

    def all_variable(self):
        """All Variable"""
        self.game_end = False
        self.wave_starting = False
        self.enemy_number = 0
        self.level_index = 0
        self.all_spawn_time_var()
        self.all_none_var()
        self.current_level_var()

    def all_spawn_time_var(self):
        """All Spawn Time Variable, use for timing and good gameplay"""
        self.sun_spawn_time = 7*FRAME
        self.enemies_first_three_spawn = 35*FRAME
        self.final_enemy_countdown = 120*FRAME

    def all_none_var(self):
        """All variable start on None"""
        self.rule_obj = None
        self.enemy_in_wave = None
        self.final_enemy_before_wave = None

    def current_level_var(self):
        """All variable controlling the level"""
        self.current_level = "LEVEL1"
        self.current_l_wave = LEVEL1
        self.current_level_w_1 = None
        self.current_level_w_2 = None
        self.current_level_w_3 = None
        self.current_level_f = LEVEL1_FINAL_WAVE
        self.current_level_trigger = LEVEL1_TRIGGER
        self.progress_num = (
            len(self.current_l_wave) + 1  # for final wave
            + (1 if self.current_level_w_1 is not None else 0)
            + (1 if self.current_level_w_2 is not None else 0)
            + (1 if self.current_level_w_3 is not None else 0))

    def all_widget(self):
        """All Important Widget used to play the game"""
        self.field = Field(self.current_level)
        self.sunslot = SunSlot(LEVEL_ALL_ENERGY)
        self.slot_holder = SlotHolder()
        self.all_fighter = Widget()
        self.all_enemies = Widget()
        self.all_sun = Widget()
        self.level_progress = LevelProgress(self.progress_num)

        self.add_widget(self.field)
        self.add_widget(self.all_fighter)
        self.add_widget(self.all_enemies)
        self.add_widget(self.sunslot)
        self.add_widget(self.slot_holder)
        self.add_widget(self.all_sun)
        self.add_widget(self.level_progress)
        self.display_message("Battle Start", "#FFFFFF")

    def start(self):
        """Start the game"""
        self.game_loop = Clock.schedule_interval(
            lambda _: self.start_loop(), 1.0/(FRAME))

    def start_loop(self):
        """Main Game Loop"""
        if self.game_end is False:
            for sun in self.all_sun.children:
                sun.update()
            for enemy in self.all_enemies.children:
                enemy.update()
            for fighters in self.all_fighter.children:
                if fighters.tile is not None:  # If fighter is not placed in tile then don't update
                    fighters.update()
            self.manage_sun()
            self.manage_enemies()

    def manage_sun(self):
        """Manage sun spawn time"""
        self.sun_spawn_time -= 1
        if self.sun_spawn_time <= 0:
            self.sun_spawn_time = 20*60
            self.all_sun.add_widget(Sun(LEVEL_ENERGY_VALUE))

    def manage_enemies(self):
        """
        Manage Enemy:
            - Spawning
            - Check Progress
            - Check If Wave
        """
        if self.enemy_in_wave is not None:
            # Check if all enemy in wave is dead, then add progress and continue
            if len(self.enemy_in_wave) == 0:
                self.level_progress.add_progress()
                self.enemy_in_wave = None
        elif self.final_enemy_before_wave is None and self.wave_starting is False:
            self.enemies_first_three_spawn -= 1
            if self.enemies_first_three_spawn <= 0:
                try:
                    # Spawn the first Three Enemy on Start
                    self.enemies_first_three_spawn = LEVEL_SCRIPT[self.enemy_number]*FRAME
                    self.add_enemy(False)
                except IndexError:
                    # If Three enemies is already spawn, then spawn enemy naturally
                    # Following the Enemy Level
                    self.enemies_first_three_spawn = (randint(35, 55))*FRAME
                    for add in range(choice(self.set_level_choice())):
                        if self.final_enemy_before_wave is None:
                            self.add_enemy(True, add)
                        else:
                            # If enemy final enemy in wave declared then break
                            break
        elif self.wave_starting is False:
            self.check_final_enemy_wave()
        elif self.current_level_f is None:
            # If Final Wave Ended then victory is achieve
            if len(self.all_enemies.children) == 0:
                self.display_message("VICTORY", "#00FF00", 64)
                self.game_end = True

    def set_level_choice(self):
        """Choice Spawn Rate Modifier"""
        if self.enemy_number <= 2:
            return LEVEL_SCRIPT_CHOICE.get("0")
        elif self.enemy_number <= 5:
            return LEVEL_SCRIPT_CHOICE.get("1")
        elif self.enemy_number <= 14:
            return LEVEL_SCRIPT_CHOICE.get("2")
        elif self.enemy_number <= 24:
            return LEVEL_SCRIPT_CHOICE.get("3")
        elif self.enemy_number <= 39:
            return LEVEL_SCRIPT_CHOICE.get("4")
        elif self.enemy_number <= 59:
            return LEVEL_SCRIPT_CHOICE.get("5")
        else:
            return LEVEL_SCRIPT_CHOICE.get("6")

    def add_enemy(self, type_=False, add_pos=0):
        """Enemy Adder, Not In Wave"""
        enemy = self.spawn_enemy_type(
            self.current_l_wave, self.level_index) if type_ else NormalEnemy()
        self.level_index += (1 if type_ else 0)
        if self.current_level_w_1 is not None:
            if self.level_index == self.current_level_trigger.get("first"):
                self.final_enemy_before_wave = enemy
        elif self.current_level_w_2 is not None:
            if self.level_index == self.current_level_trigger.get("second"):
                self.final_enemy_before_wave = enemy
        elif self.current_level_w_3 is not None:
            if self.level_index == self.current_level_trigger.get("third"):
                self.final_enemy_before_wave = enemy
        elif self.current_level_f is not None:
            if self.level_index == self.current_level_trigger.get("final"):
                self.final_enemy_before_wave = enemy
        self.spawn_enemy(enemy, add_pos)

    def spawn_enemy(self, enemy, add_pos=0):
        """Spawn an Enemy"""
        self.all_enemies.add_widget(enemy)
        enemy.set_position()
        enemy.x += (enemy.width/(randint(4, 16)))*add_pos
        self.enemy_number += 1

    def spawn_enemy_type(self, enemy_type, index=None):
        """Check Enemy Type"""
        if ALL_ENEMY_TYPE.get(enemy_type[index] if index is not None else enemy_type) == "ordinary":
            return NormalEnemy()
        else:
            return NormalEnemy()

    def check_final_enemy_wave(self):
        """Check if all enemies dead, ot timer on final enemy count down is zero the wave is going to execute"""
        if len(self.all_enemies.children) == 0 or self.final_enemy_countdown <= 0:
            self.wave_func()
            self.final_enemy_before_wave = None
            self.final_enemy_countdown = 120*FRAME
            return True
        self.final_enemy_countdown -= 1

    def wave_func(self):
        """When wave is happening"""
        self.wave_starting = True
        self.display_message("Warning: A huge army of enemy is coming!")
        if self.current_level_w_1 is None and self.current_level_w_2 is None and self.current_level_w_3 is None:
            Clock.schedule_once(lambda _: self.display_message(
                "FINAL WAVE", "#FF0000", 64), 4)
            Clock.schedule_once(lambda _: self.wave_attack(), 8)
        else:
            Clock.schedule_once(lambda _: self.wave_attack(), 5)

    def display_message(self, text=None, color=None, size=None):
        """Automatically display message"""
        message = Message()
        message.lab.color = gc(
            color) if color is not None else message.lab.color
        message.lab.font_size = sp(
            size) if size is not None else message.lab.font_size
        message.lab.text = text if text is not None else ""
        self.add_widget(message)

    def wave_attack(self):
        """Spawn all enemy in wave"""
        if self.current_level_w_1 is not None:
            self.iterate_spawner(self.current_level_w_1)
            self.current_level_w_1 = None
        elif self.current_level_w_2 is not None:
            self.iterate_spawner(self.current_level_w_2)
            self.current_level_w_2 = None
        elif self.current_level_w_3 is not None:
            self.iterate_spawner(self.current_level_w_3)
            self.current_level_w_3 = None
        elif self.current_level_f is not None:
            self.iterate_spawner(self.current_level_f)
            self.current_level_f = None
            return True
        self.wave_starting = False

    def iterate_spawner(self, wave) -> None:
        """Iterate Enemy"""
        self.enemy_in_wave = list()
        for index, it in enumerate(wave):
            enemy = self.spawn_enemy_type(it)
            self.spawn_enemy(enemy, index)
            self.enemy_in_wave.append(enemy)

    def reset_level(self):
        """Reset Level"""
        self.clear_widgets()
        self.all_sun.clear_widgets()
        self.all_enemies.clear_widgets()
        self.all_fighter.clear_widgets()
