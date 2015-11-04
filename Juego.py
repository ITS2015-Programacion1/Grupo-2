# coding: utf-8
import pilasengine

pilas=pilasengine.iniciar()

fondo=pilas.fondos.Pasto()



def iniciar_juego():
    fondo.eliminar()
    menu.eliminar()
    puntos = pilas.actores.Puntaje(x=230, y=200, color=pilas.colores.naranja)
    puntos.magnitud = 40
    pilas.actores.Sonido()
    
    mapa = pilas.actores.MapaTiled("mapajuego.tmx")
    personaje=pilas.actores.Maton()
    personaje.y=-200


    

    

        

def opciones():
    pilas.fondos.Noche()
    menu.eliminar()
    menu2=pilas.actores.Menu
    text=pilas.actores.Texto("Como jugar:")
    text.y=200
    text2=pilas.actores.Texto("-Mover el personaje con las flechas")
    text2.y=165
    text3=pilas.actores.Texto("-Objetivo: Lograr pasar todos los obstaculos de dicho nivel sin perder la vida")
    text3.y=100
    text3.escala = .7
def salir_juego():
    pilas.terminar()


menu=pilas.actores.Menu(
    [
        ("iniciar juego", iniciar_juego),
        ("opciones", opciones),
        ("salir", salir_juego)
    ])  




pilas.ejecutar()
