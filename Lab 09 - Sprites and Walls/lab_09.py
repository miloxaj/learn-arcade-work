import arcade
import random

# Definimos el tamaño de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definimos el tamaño de cada sprite
SPRITE_SIZE = 0.5

# Definimos la velocidad del jugador
PLAYER_MOVEMENT_SPEED = 5

# Definimos la cantidad de monedas
COIN_COUNT = 50

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_WIDTH, "Mi juego")
        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None
        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        # Definimos el color de fondo
        arcade.set_background_color(arcade.color.AMAZON)

        # Creamos el sprite del jugador
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_walk0.png")
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2

        # Creamos una lista de sprites para las monedas
        self.coin_list = arcade.SpriteList()

        # Creamos las monedas y las añadimos a la lista
        for i in range(COIN_COUNT):
            coin = arcade.Sprite(":resources:images/items/gold_1.png", 0.3)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)

        # Creamos una lista de sprites para las paredes
        self.wall_list = arcade.SpriteList()

        # Creamos las paredes y las añadimos a la lista
        for x in range(0,SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", 1)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

            wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", 1)
            wall.center_x = x
            wall.center_y = SCREEN_HEIGHT - SPRITE_SIZE
            self.wall_list.append(wall)

        for y in range(SPITE_SIZE, SCREEN_HEIRGHT - SPRITE_SIZE, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", 1)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

            wall = arcade.Sprite("images/wall.png", 1)
            wall.center_x = SCREEN_WIDTH - SPRITE_SIZE
            wall.center_y = y
            self.wall_list.append(wall)

    def on_draw(self):
        arcade.start_render()
        self.camera_for_sprites.use()
        # Dibujamos todos los sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_sprite.draw()
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def update(self, delta_time):
        # Movemos al jugador
        if arcade.key.LEFT in self.keys_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif arcade.key.RIGHT in self.keys_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

        if arcade.key.UP in self.keys_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif arcade.key.DOWN in self.keys_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()