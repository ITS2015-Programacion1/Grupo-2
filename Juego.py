# coding: utf-8
import pilasengine

pilas=pilasengine.iniciar()

fondo=pilas.fondos.Pasto()




def iniciar_juego():
    pilas.fondos.Galaxia()
    menu.eliminar()
    puntos = pilas.actores.Puntaje(x=230, y=200, color=pilas.colores.naranja)
    puntos.magnitud = 40
    pilas.actores.Sonido()
    estrella=pilas.actores.Estrella(x=50)
    
    class personaje(pilasengine.actores.Calvo):
          
          def crear_personaje(self):
              personaje=pilas.actores.Calvo()
              self.escala=0.0
              
         
                           
              

    pilas.actores.vincular(personaje)
    personaje=pilas.actores.personaje()
    

def opciones():
    pilas.fondos.Noche()
    menu.eliminar()
    menu2=pilas.actores.Menu
    text=pilas.actores.Texto("Como jugar:")
    text.y=200
    text2=pilas.actores.Texto("-Mover el personaje con las flechas")
    text2.y=165
    

def salir_juego():
    pilas.terminar()


menu=pilas.actores.Menu(
    [
        ("iniciar juego", iniciar_juego),
        ("opciones", opciones),
        ("salir", salir_juego)
    ])  



 

pilas.ejecutar()
