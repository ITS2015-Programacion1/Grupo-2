# coding: utf-8
import pilasengine
import random


pilas=pilasengine.iniciar()
fondo=pilas.actores.MapaTiled('mapajuego.tmx')
puntos=pilas.actores.Puntaje(x=230, y=200, color=pilas.colores.negro)
pilas.fisica.eliminar_techo()
pilas.fisica.eliminar_suelo()
pilas.fisica.eliminar_paredes()
pilas.actores.Sonido()
class SaltarUnaVez(pilas.comportamientos.Comportamiento):

      def iniciar(self, receptor, velocidad_inicial=5, cuando_termina=None):

            super(SaltarUnaVez, self).iniciar(receptor)
            self.velocidad_inicial = velocidad_inicial
            self.cuando_termina = cuando_termina
            self.sonido_saltar = self.pilas.sonidos.cargar("audio/saltar.wav")
            self.suelo = int(self.receptor.y)
            self.velocidad = self.velocidad_inicial
            self.sonido_saltar.reproducir()
            self.velocidad_aux = self.velocidad_inicial
            self.receptor.saltando = True
           

      def actualizar(self):
          self.receptor.y += self.velocidad
          self.velocidad -= 0.3
         
        

          if self.receptor.y <= self.suelo:
             self.velocidad_aux /= 3.5
             self.velocidad = self.velocidad_aux


             if self.velocidad_aux <= 1:
                self.receptor.y = self.suelo
                if self.cuando_termina:
                   self.cuando_termina()
                self.receptor.saltando = False
                return True
teclas = {
            pilas.simbolos.a: 'izquierda',
            pilas.simbolos.d: 'derecha',
            pilas.simbolos.w: 'arriba',
            pilas.simbolos.s: 'abajo',
            pilas.simbolos.ESPACIO: 'boton',
        }
mi_control = pilas.control.Control(teclas)

class Personaje(pilasengine.actores.Actor):
      
      def iniciar(self):
          self.imagen="personaje.png"
          self.radio_de_colison= 100
          self.escala=0.4
          self.y= -197.6
          self.x= -5515.1
          self.figura = pilas.fisica.Circulo(self.x, self.y, 27,
            friccion=0, restitucion=0)
          self.figura.sin_rotacion = True
          self.figura.escala_de_gravedad = 2
          self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)
          self.saltando = False
         

          

      def actualizar(self):
          pilas.camara.x=self.x	
          velocidad = 7
          salto = 20
          self.x = self.figura.x
          self.y = self.figura.y
          if self.pilas.control.derecha:
            self.figura.velocidad_x = velocidad
            self.rotacion -= velocidad
          elif self.pilas.control.izquierda:
              self.figura.velocidad_x = -velocidad
              self.rotacion += velocidad
          else:
              self.figura.velocidad_x = 0

          if self.esta_pisando_el_suelo():
              if self.pilas.control.arriba and int(self.figura.velocidad_y) <= 0:
                  self.figura.impulsar(0, salto)

          self.sensor_pies.x = self.x
          self.sensor_pies.y = self.y - 20
        
          if self.esta_pisando_el_suelo():
              self.imagen = "personaje.png"
          else:
              self.imagen = "personaje.png"

        
      def esta_pisando_el_suelo(self):
          return len(self.sensor_pies.figuras_en_contacto) > 0


               
          if self.pilas.escena_actual().control.arriba:
             if not self.saltando:
                    self.hacer("SaltarUnaVez")


pilas.actores.vincular(Personaje)
protagonista = pilas.actores.Personaje()



#actores

class Enemigos(pilasengine.actores.Actor):
      
      def iniciar(self):
          self.imagen="mono.png"
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= -300:
             self.direccion=1
             self.espejado = False
          if self.x >= 300:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5

pilas.actores.vincular(Enemigos)
enemigo=pilas.actores.Enemigos()

def choque(enemigo, protagonista):
    

pilas.colisiones.agregar(enemigo, protagonista, choque)
lanzador= Enemigos(pilas)
lanzador.escala_x= .4
lanzador.escala_y= .4
pilas.comportamientos.vincular(SaltarUnaVez)
personaje_salto = Personaje(pilas)
pilas.ejecutar()
