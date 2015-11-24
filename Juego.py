# coding: utf-8
import pilasengine
import random
import math

pilas=pilasengine.iniciar()
fondo=pilas.actores.MapaTiled('mapajuego.tmx')
pilas.fisica.eliminar_techo()
pilas.fisica.eliminar_paredes()
pilas.fisica.eliminar_suelo()
fin_de_juego = False
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

class Colisiones(pilas.actores.Actor):
    def iniciar(self):
        self.imagen=("pared.png")
        self.caida=pilas.fisica.Rectangulo(10.7,-225,11050,35, sensor=True, dinamica=False)
           


class Otro(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "pared.png"


class Personaje(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="aceituna.png"
          self.y= -158.9
          self.x= -5513.0
          self.figura = pilas.fisica.Circulo(self.x, self.y, 17,
            friccion=0, restitucion=0)
          self.figura.sin_rotacion = True
          self.figura.escala_de_gravedad = 2
          self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)
          self.escala = 1
          self.aprender(pilas.habilidades.PuedeExplotarConHumo)
          self.aprender(pilas.habilidades.Arrastrable)
          self.radio_de_colision=157
          self.radio_de_colision=16
          self.espejado=False
          self.saltando = False
          
          

      

          

      def actualizar(self):
          velocidad = 9
          salto = 7
          self.x = self.figura.x
          self.y = self.figura.y
          pilas.camara.x=self.x	
          if self.pilas.escena_actual().control.izquierda:
             self.espejado = False
             self.x -= 4
          elif self.pilas.escena_actual().control.derecha:
               self.x += 4
               self.espejado = True
               
          if self.pilas.escena_actual().control.arriba:
             if not self.saltando:
                    self.hacer("SaltarUnaVez")

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
        
          

        
      def esta_pisando_el_suelo(self):
          return len(self.sensor_pies.figuras_en_contacto) > 0




#actores

class Enemigos(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=-4817.4
          self.y=-30.9
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= -4817.4:
             self.direccion=1
             self.espejado = False
          if self.x >= -4564.4:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5

enemigo = Enemigos(pilas)
enemigo.escala=0
pilas.actores.vincular(Personaje)
personaje = Personaje(pilas)
pilas.actores.vincular(Otro)
otro = Otro(pilas)
otro.escala_x = 0
otro.escala_y = 0

pilas.actores.vincular(Enemigos)

def Prueba(personaje, enemigo):
    personaje.eliminar()



def Morir_con_pinches(personaje, otro):
    print "Hola"

pilas.colisiones.agregar(personaje, otro ,Morir_con_pinches)
pilas.colisiones.agregar(personaje, caida, Morir_con_pinches)
pilas.colisiones.agregar(personaje, enemigo, Prueba)
lanzador= Enemigos(pilas)
lanzador.escala_x= .4
lanzador.escala_y= .4
pilas.comportamientos.vincular(SaltarUnaVez)
"personaje_salto = Personaje(pilas)"
pilas.ejecutar()
  
