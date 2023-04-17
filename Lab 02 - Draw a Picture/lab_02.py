#Esto es un programa de prueba donde practicaremos y aprenderemos a crear dibujos como cuadrados,
#triangulos ,circulos,etc.
import arcade
arcade.open_window(700, 600, "Drawing Example")
arcade.set_background_color(arcade.color.LIGHT_YELLOW)

arcade.start_render()
arcade.draw_rectangle_filled(300,225, 600, 100, arcade.csscolor.SIENNA)
arcade.draw_rectangle_filled(650,350, 200, 350, arcade.csscolor.DARK_GREY)
arcade.draw_rectangle_filled(50,350, 200, 350, arcade.csscolor.DARK_GREY)
arcade.draw_rectangle_filled(350,275, 150, 25, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(350,300, 25, 75, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(350,400, 350, 200, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(350,400, 330, 175, arcade.csscolor.LIGHT_BLUE)
arcade.draw_circle_filled(70, 450, 50, arcade.csscolor.GREY)
arcade.draw_circle_filled(70, 350, 50, arcade.csscolor.GREY)
arcade.draw_circle_filled(70, 250, 50, arcade.csscolor.GREY)
arcade.draw_circle_filled(625, 450, 50, arcade.csscolor.GREY)
arcade.draw_circle_filled(625, 350, 50, arcade.csscolor.GREY)
arcade.draw_circle_filled(625, 250, 50, arcade.csscolor.GREY)
arcade.draw_circle_filled(300, 125, 30, arcade.csscolor.BLACK)
arcade.draw_circle_filled(370, 125, 30, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(330,125, 75, 25, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(300, 115, 60, 80, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(370, 115, 60, 80, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(300,150, 30, 15, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(370,150, 30, 15, arcade.csscolor.BLACK)
arcade.draw_circle_filled(370, 115, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(370, 135, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(360, 125, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(380, 125, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(300, 115, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(300, 135, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(290, 125, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(310, 125, 5, arcade.csscolor.WHITE)



arcade.finish_render()
arcade.run()