""" Lab 7 - User Control """

import arcade
import self as self

# --- Constants ---
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
def draw_floor():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.BROWN_NOSE)

def draw_speaker():
    arcade.draw_rectangle_filled(650, 350, 200, 350, arcade.csscolor.DARK_GREY)
    arcade.draw_rectangle_filled(50, 350, 200, 350, arcade.csscolor.DARK_GREY)
    arcade.draw_circle_filled(70, 450, 50, arcade.csscolor.GREY)
    arcade.draw_circle_filled(70, 350, 50, arcade.csscolor.GREY)
    arcade.draw_circle_filled(70, 250, 50, arcade.csscolor.GREY)
    arcade.draw_circle_filled(625, 450, 50, arcade.csscolor.GREY)
    arcade.draw_circle_filled(625, 350, 50, arcade.csscolor.GREY)
    arcade.draw_circle_filled(625, 250, 50, arcade.csscolor.GREY)
def table():
    arcade.draw_rectangle_filled(300, 225, 600, 100, arcade.csscolor.SIENNA)

def tv():
    arcade.draw_rectangle_filled(350, 275, 150, 25, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(350, 300, 25, 75, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(350, 400, 350, 200, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(350, 400, 330, 175, arcade.csscolor.LIGHT_BLUE)


class Ellipse:
    def __init__(self, position_x, position_y, width,height, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height=height
        self.color = color
    def draw(self):
        """ Draw the ellipse with the instance variables we have. """
        arcade.draw_ellipse_filled(self.position_x,self.position_y,self.width,self.height,self.color)
class Rectangle:
    def __init__(self, position_x, position_y,change_x, change_y, width, height, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.change_x = change_x
        self.change_y = change_y
        self.height = height
        self.color = color

    def draw(self):
        """ Draw the ellipse with the instance variables we have. """
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.width:
            self.position_x = self.width

        if self.position_x > SCREEN_WIDTH - self.width:
            self.position_x = SCREEN_WIDTH - self.width

        if self.position_y < self.width:
            self.position_y = self.width

        if self.position_y > SCREEN_HEIGHT - self.width:
            self.position_y = SCREEN_HEIGHT - self.width
class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BEIGE)
    #CREATE OUR ELLIPSE

        self.ellipse= Ellipse(150,100,100,200,arcade.color.GREEN_YELLOW)
        self.rectangle= Rectangle(350,200,0,0,100,200,arcade.color.PURPLE_NAVY)
    def on_draw(self):
        arcade.start_render()
        draw_floor()
        table()
        draw_speaker()
        # TV
        tv()
        self.ellipse.draw()
        self.rectangle.draw()

    def update(self, delta_time):
        self.rectangle.update()
    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ellipse.position_x = x
        self.ellipse.position_y = y
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.rectangle.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.rectangle.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.rectangle.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.rectangle.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.rectangle.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.rectangle.change_y = 0

def main():
    window = MyGame()
    arcade.run()


main()