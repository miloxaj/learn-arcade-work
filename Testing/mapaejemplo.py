import arcade
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"
class MyGame(arcade.Window):

    def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    self.tile_map = None
    arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):