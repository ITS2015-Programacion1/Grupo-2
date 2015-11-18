# coding: utf-8
import pilasengine
import random
import math

pilas=pilasengine.iniciar()
fondo=pilas.actores.MapaTiled('mapajuego.tmx')
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
          self.imagen = "aceituna.png"
          self.escala=1
          self.escala = 1
          self.y=-100
          self.radio_de_colision=157
          self.aprender(pilas.habilidades.Disparar)
          self.radio_de_colision=16
          self.espejado=True
          self.saltando = False
          
          

      

          

      def actualizar(self):
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


pilas.actores.vincular(Personaje)
protagonista = pilas.actores.Personaje()
rect1 = pilas.fisica.Rectangulo(0,-100,10,10)
protagonista.aprender(pilas.habilidades.Imitar,rect1)



#actores

class Enemigos(pilasengine.actores.Mono):
      def iniciar(self):
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
pelo = pilas.actores.Pelota()

lanzador= Enemigos(pilas)
lanzador.escala_x= .4
lanzador.escala_y= .4
pilas.comportamientos.vincular(SaltarUnaVez)
personaje_salto = Personaje(pilas)
pilas.ejecutar()
