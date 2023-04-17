#Esto es un programa de prueba donde practicaremos y aprenderemos a crear dibujos como cuadrados,
#triangulos ,circulos,etc.
import arcade
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
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
def ps_controller(x,y):
    arcade.draw_point(x, y, arcade.color.RED, 5)
    arcade.draw_circle_filled(300+x, 125+y, 30, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(370+x, 125+y, 30, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(330+x, 125+y, 75, 25, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(300+x, 115, 60+y, 80, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(370+x, 115, 60+y, 80, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(300+x, 150+y, 30, 15, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(370+x, 150+y, 30, 15, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(370+x, 115+y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(370+x, 135+y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(360+x, 125+y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(380+x, 125+y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(300+x, 115+y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(300+x, 135+y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(290+x, 125+y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(310+x, 125+y, 5, arcade.csscolor.WHITE)
def tv():
    arcade.draw_rectangle_filled(350, 275, 150, 25, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(350, 300, 25, 75, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(350, 400, 350, 200, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(350, 400, 330, 175, arcade.csscolor.LIGHT_BLUE)
def on_draw(delta_time):
    arcade.start_render()
    draw_floor()
    table()
    draw_speaker()
    # TV
    tv()
    # ps controller
    ps_controller(on_draw.ps_controller1_x,0)
    ps_controller(0, 0)
    arcade.finish_render()
    on_draw.ps_controller1_x+=1

on_draw.ps_controller1_x=150


def main():
    #background
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with functions")
    arcade.set_background_color(arcade.color.LIGHT_YELLOW)
    # finish and run
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


main()