import pilasengine

pilas = pilasengine.iniciar()

mapa = pilas.actores.MapaTiled('mapajuego.tmx')

# Genera un personaje en movimiento.



pilas.avisar("Use el teclado para mover al personaje.")
class Personaje(pilasengine.actores.Maton):
      def iniciar(self):
          self.imagen = self.pilas.imagenes.cargar_grilla("rpg/maton.png", 3, 4)
          self.figura=self.pilas.fisica.Rectangulo(self.x, self.y, 20, 33, friccion=0,restitucion=0)
          self.figura.sin_rotacion=True
          self.sensor_pies = self.pilas.fisica.Rectangulo(self.x, self.y, 10, 5, sensor=True, dinamica=False)
          self.escala=1
          self.escala = 1
          self.y=-100
          self.radio_de_colision=157
          self.aprender(pilas.habilidades.Disparar)
          self.radio_de_colision=16
          self.espejado=True
          self.figura = pilas.fisica.Rectangulo(self.x, self.y, 40, 80, friccion=0, restitucion=0)
          self.figura.sin_rotacion = True
          self.figura.escala_de_gravedad = 2
          self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 2, 5, sensor=True, dinamica=False)
          self.saltando = False
          self.saltando = False
          pilas.camara.x=self.x	

      

          

      def actualizar(self):
          if self.pilas.escena_actual().control.izquierda:
             self.espejado = False
             self.x -= 4
          elif self.pilas.escena_actual().control.derecha:
               self.x += 4
               self.espejado = True

          if self.pilas.escena_actual().control.arriba:
             if not self.saltando:
                    self.hacer("SaltarUnaVez")


pilas.actores.vincular(Personaje)
protagonista = pilas.actores.Personaje()

pilas.ejecutar()
