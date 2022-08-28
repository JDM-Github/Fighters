from configuration import WIDTH, HEIGHT
from kivy.uix.image import Image
from kivy.metrics import dp


class LevelProgress(Image):

    def __init__(self, num, **kwargs):
        super().__init__(**kwargs)
        self.size = WIDTH*0.3, HEIGHT*0.05
        self.pos = (WIDTH*0.7)-dp(10), dp(10)
        self.progress_size = self.width/(num+3)
        self.display_progress()

    def display_progress(self):
        self.progress = Image()
        self.progress.color = (0, 1, 0, 1)
        self.progress.pos = self.pos
        self.progress.size = 0, self.height
        self.add_widget(self.progress)

    def add_progress(self):
        self.progress.width += self.progress_size
