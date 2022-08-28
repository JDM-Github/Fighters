from configuration import LANE, TILE, WIDTH, HEIGHT
from kivy.uix.gridlayout import GridLayout
from tiles import NoTile, NormalTile


class Lane(GridLayout):
    """Laning use for the game"""

    def __init__(self, type="normal", row_pos: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.type = type
        self.rows = 1
        self.cols = TILE
        self.row_pos = row_pos
        self.size = ((WIDTH*0.8),
                     ((HEIGHT*0.8)/LANE))
        self.pos = ((WIDTH*0.2), (HEIGHT*0.05) +
                    (((HEIGHT*0.8)/LANE)*row_pos))
        self.lane_row = row_pos
        self.all_tile = list()
        self.display_field()

    def display_field(self):
        """Display The Field"""
        for i in range(TILE):
            if self.type == "normal":
                setattr(self, f"tile{i}", NormalTile(i+self.row_pos, i))
                self.all_tile.append(getattr(self, f"tile{i}"))
                self.add_widget(getattr(self, f"tile{i}"))
            else:
                setattr(self, f"tile{i}", NoTile(i))
                self.all_tile.append(getattr(self, f"tile{i}"))
                self.add_widget(getattr(self, f"tile{i}"))
