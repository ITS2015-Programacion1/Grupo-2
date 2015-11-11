# coding: utf-8
import pilasengine
import random
import math

pilas=pilasengine.iniciar()
fondo=pilas.fondos.Pasto()

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

class PersonajeConControles(pilasengine.actores.aceituna.Aceituna):
      def iniciar(self):
          self.escala = 1
          self.radio_de_colision=157
          self.aprender(pilas.habilidades.Disparar)
          self.radio_de_colision=16

          self.saltando = False

      def actualizar(self):
          if self.pilas.escena_actual().control.izquierda:
             self.x -= 4
          elif self.pilas.escena_actual().control.derecha:
               self.x += 4

          if self.pilas.escena_actual().control.arriba:
             if not self.saltando:
                    self.hacer("SaltarUnaVez")
     

#actores

class enemigos(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen = "alien.png"
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
    


        
lanzador= enemigos(pilas)
lanzador.escala_x= .4
lanzador.escala_y= .4
pilas.comportamientos.vincular(SaltarUnaVez)
personaje_salto = PersonajeConControles(pilas)
pilas.ejecutar()
