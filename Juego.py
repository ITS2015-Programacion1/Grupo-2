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


    
           
class Otro(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "pared.png"
        self.escala_x=0
        self.escala_y=0 



class Personaje(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="personaje.png"
          self.y= -158.9
          self.x= -5513.0
          self.figura = pilas.fisica.Circulo(self.x, self.y, 20,
            friccion=0, restitucion=0)
          self.figura.sin_rotacion = True
          self.figura.escala_de_gravedad = 2
          self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)
          self.escala = 0.3
          self.aprender(pilas.habilidades.PuedeExplotarConHumo)
          self.aprender(pilas.habilidades.Arrastrable)
          self.radio_de_colision=157
          self.radio_de_colision=16
          self.espejado=False
          self.saltando = False
          
          

      

          

      def actualizar(self):
          velocidad = 7
          salto = 6.5
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

class Enemigos2(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=-2205.2
          self.y=97.2
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= -2205.2:
             self.direccion=1
             self.espejado = False
          if self.x >= -1735.1:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5

class Enemigos3(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=-1139.5
          self.y=65.1
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= -1139.5:
             self.direccion=1
             self.espejado = False
          if self.x >= -884.0:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5
class Enemigos4(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=-1614.9
          self.y=30.9
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <=-1614.9 :
             self.direccion=1
             self.espejado = False
          if self.x >=-1344.6:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5
class Enemigos5(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=-121.6
          self.y=-62.9
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= -121.6:
             self.direccion=1
             self.espejado = False
          if self.x >= 83.2:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5
class Enemigos6(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=1000
          self.y=161.1
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <=1000 :
             self.direccion=1
             self.espejado = False
          if self.x >= 1309.8:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5
class Enemigos7(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=1456.9
          self.y=33.3
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <=1456.9 :
             self.direccion=1
             self.espejado = False
          if self.x >=1742.6 :
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5      
class Enemigos8(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=1937.1
          self.y=-126.9
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <=1937.1 :
             self.direccion=1
             self.espejado = False
          if self.x >=2356.7:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5
class Enemigos9(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=3148.5
          self.y=33.3
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= 3148.5:
             self.direccion=1
             self.espejado = False
          if self.x >= 3318.5:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5
class Enemigos10(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=3504.7
          self.y=97.1
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= 3504.7:
             self.direccion=1
             self.espejado = False
          if self.x >= 3696.5:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5
class Enemigos11(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=3825.1
          self.y=1.1
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= 3825.1:
             self.direccion=1
             self.espejado = False
          if self.x >= 4142.9:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5
class Enemigos12(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=4262.9
          self.y=129.2
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= 4262.9:
             self.direccion=1
             self.espejado = False
          if self.x >= 4789.8:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5
class Enemigos13(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=5029.7
          self.y=33.1
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= 5029.7:
             self.direccion=1
             self.espejado = False
          if self.x >= 5239.7:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5

class Enemigos14(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=-1614.9
          self.y=-30.9
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.x <= -1614.9:
             self.direccion=1
             self.espejado = False
          if self.x >= -1354.9:
             self.direccion=-1
             self.espejado = True
          self.x+=self.direccion * 5

class Enemigos15(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=5360.9
          self.y=-190.9
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.y <= -190.9:
             self.direccion=1
             self.espejado = False
          if self.y >= 190.9:
             self.direccion=-1
             self.espejado = True
          self.y+=self.direccion * 5          

class Enemigos16(pilasengine.actores.Actor):
      def iniciar(self):
          self.imagen="mono.png"
          self.radio_de_colision=20
          self.x=5360.9
          self.y=190.9
          self.direccion=-1
          self.espejado=True

      def actualizar(self):
          if self.y <= 190.9:
             self.direccion=1
             self.espejado = False
          if self.y >= -190.9:
             self.direccion=-1
             self.espejado = True
          self.y+=self.direccion * 5



enemigo= Enemigos(pilas)
enemigo2= Enemigos2(pilas)
enemigo3= Enemigos3(pilas)
enemigo4= Enemigos4(pilas)
enemigo5= Enemigos5(pilas)
enemigo6= Enemigos6(pilas)
enemigo7= Enemigos7(pilas)
enemigo8= Enemigos8(pilas)
enemigo9= Enemigos9(pilas)
enemigo10= Enemigos10(pilas)
enemigo11= Enemigos11(pilas)
enemigo12= Enemigos12(pilas)
enemigo13= Enemigos13(pilas)
enemigo14= Enemigos14(pilas)
enemigo15= Enemigos15(pilas)
enemigo16= Enemigos16(pilas)



enemigo.escala=0
enemigo2.escala =0
enemigo3.escala=0
enemigo4.escala=0
enemigo5.escala =0
enemigo6.escala=0
enemigo7.escala=0
enemigo8.escala =0
enemigo9.escala=0
enemigo10.escala=0
enemigo11.escala =0
enemigo12.escala=0
enemigo13.escala=0
enemigo14.escala=0
enemigo15.escala=0
enemigo16.escala=0

pilas.actores.vincular(Otro)
otro = Otro(pilas)
otro.escala_x = 0
otro.escala_y = 0
otro.x=9.7
otro.y=-221
caida=pilas.fisica.Rectangulo(10.7,-225,11500,35, sensor=True, dinamica=False)
otro.figura_de_colision=caida


pilas.actores.vincular(Personaje)
personaje = Personaje(pilas)



pilas.actores.vincular(Enemigos)
pilas.actores.vincular(Enemigos2)
pilas.actores.vincular(Enemigos3)
pilas.actores.vincular(Enemigos4)
pilas.actores.vincular(Enemigos5)
pilas.actores.vincular(Enemigos6)
pilas.actores.vincular(Enemigos7)
pilas.actores.vincular(Enemigos8)
pilas.actores.vincular(Enemigos9)
pilas.actores.vincular(Enemigos10)
pilas.actores.vincular(Enemigos11)
pilas.actores.vincular(Enemigos12)
pilas.actores.vincular(Enemigos13)
pilas.actores.vincular(Enemigos14)
pilas.actores.vincular(Enemigos15)
pilas.actores.vincular(Enemigos16)


def Prueba():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba2():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba3():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba4():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba5():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba6():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba7():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba8():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba9():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba10():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba11():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba12():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba13():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba14():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba15():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9
def Prueba16():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9   
def Morir_con_pinches():
    global personaje
    personaje.figura.x=-5429.7
    personaje.figura.y=-126.9  

pilas.colisiones.agregar(personaje, otro, Morir_con_pinches)
pilas.colisiones.agregar(personaje, enemigo, Prueba)
pilas.colisiones.agregar(personaje, enemigo2, Prueba2)
pilas.colisiones.agregar(personaje, enemigo3, Prueba3)
pilas.colisiones.agregar(personaje, enemigo4, Prueba4)
pilas.colisiones.agregar(personaje, enemigo5, Prueba5)
pilas.colisiones.agregar(personaje, enemigo6, Prueba6)
pilas.colisiones.agregar(personaje, enemigo7, Prueba7)
pilas.colisiones.agregar(personaje, enemigo8, Prueba8)
pilas.colisiones.agregar(personaje, enemigo9, Prueba9)
pilas.colisiones.agregar(personaje, enemigo10, Prueba10)
pilas.colisiones.agregar(personaje, enemigo11, Prueba11)
pilas.colisiones.agregar(personaje, enemigo12, Prueba12)
pilas.colisiones.agregar(personaje, enemigo13, Prueba13)
pilas.colisiones.agregar(personaje, enemigo14, Prueba14)
pilas.colisiones.agregar(personaje, enemigo15, Prueba15)
pilas.colisiones.agregar(personaje, enemigo16, Prueba16)



lanzador= Enemigos(pilas)
lanzador.escala_x= .4
lanzador.escala_y= .4
lanzador2= Enemigos2(pilas)
lanzador2.escala_x= .4
lanzador2.escala_y= .4
lanzador3= Enemigos3(pilas)
lanzador3.escala_x= .4
lanzador3.escala_y= .4
lanzador4= Enemigos3(pilas)
lanzador4.escala_x= .4
lanzador4.escala_y= .4
lanzador5= Enemigos5(pilas)
lanzador5.escala_x= .4
lanzador5.escala_y= .4
lanzador6= Enemigos6(pilas)
lanzador6.escala_x= .4
lanzador6.escala_y= .4
lanzador7= Enemigos7(pilas)
lanzador7.escala_x= .4
lanzador7.escala_y= .4
lanzador8= Enemigos8(pilas)
lanzador8.escala_x= .4
lanzador8.escala_y= .4
lanzador9= Enemigos9(pilas)
lanzador9.escala_x= .4
lanzador9.escala_y= .4
lanzador10= Enemigos10(pilas)
lanzador10.escala_x= .4
lanzador10.escala_y= .4
lanzador11= Enemigos11(pilas)
lanzador11.escala_x= .4
lanzador11.escala_y= .4
lanzador12= Enemigos12(pilas)
lanzador12.escala_x= .4
lanzador12.escala_y= .4
lanzador13= Enemigos13(pilas)
lanzador13.escala_x= .4
lanzador13.escala_y= .4
lanzador14= Enemigos14(pilas)
lanzador14.escala_x= .4
lanzador14.escala_y= .4
lanzador15= Enemigos15(pilas)
lanzador15.escala_x= .4
lanzador15.escala_y= .4
lanzador16= Enemigos16(pilas)
lanzador16.escala_x= .4
lanzador16.escala_y= .4





pilas.comportamientos.vincular(SaltarUnaVez)
"personaje_salto = Personaje(pilas)"
pilas.ejecutar()
  
