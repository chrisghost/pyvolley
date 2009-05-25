# coding=UTF-8
from PySFML import sf

import menu
import pers
import ball
import obstacle
import moteur_particule
import moteur_collision

#Création de la fenêtre
window = sf.RenderWindow(sf.VideoMode(800, 600), "pyVolley")
#limitation des FPS
window.SetFramerateLimit(100)

#Optimisation
window.PreserveOpenGLStates(False) #OptimizeForNonOpenGL(True)

#cache le pointeur de la souris
window.ShowMouseCursor(False)

i = sf.Image()
i.LoadFromFile("img/loading.png")
s = sf.Sprite(i)
window.Draw(s)
window.Display()

#Création du menu
menu = menu.menu(window)
