import arcade
import pytmx

class Mapa:
    def __init__(self, archivo_tmx):
        self.mapa = pytmx.TiledMap(archivo_tmx)
        self.ancho = self.mapa.width * self.mapa.tilewidth
        self.alto = self.mapa.height * self.mapa.tileheight

    def dibujar(self):
        for capa in self.mapa.visible_layers:
            if isinstance(capa, pytmx.TiledTileLayer):
                for x, y, gid in capa:
                    tile = self.mapa.get_tile_image_by_gid(gid)
                    arcade.draw_xywh_rectangle_textured(x * self.mapa.tilewidth,
                                                         (self.mapa.height - y - 1) * self.mapa.tileheight,
                                                         self.mapa.tilewidth, self.mapa.tileheight, tile)

class MiJuego(arcade.Window):
    def __init__(self, ancho, alto, titulo):
        super().__init__(ancho, alto, titulo)
        arcade.set_background_color(arcade.color.AMAZON)

        self.mapa = Mapa("mapa.tmx")

    def on_draw(self):
        arcade.start_render()
        self.mapa.dibujar()

juego = MiJuego(800, 600, "Mi Juego")
arcade.run()
