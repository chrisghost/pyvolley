# coding=UTF-8
from PySFML import sf
import anim
import cmath
import boule

class Ball(boule.Boule):
	"""
    jump = False
    img = sf.Image()
    force_img = sf.Image()
    barre_energie = sf.Image()
    barre_energie_vide = sf.Image()

    velx = 20
    vely = 20
    vel_moving = 8
    vel_grav = 0.2
    sol = 100
    vel_jumping = 10
    screen_width = 800
    screen_height = 600
    impact = 0
    force = -1
    energie = 0
    niveau_gauge_energie = 0
    p=complex()

    keys = []
    time_update = 0
    time = 0
    feu = False

    immobilisation = 0
    moteur_p = 0
    velx_prec = 0
"""
	def __init__(self, m, r, p0=complex(200, 300), v0=complex(0, 122), a0=complex(0, 0.15), friction=0.5, bounce_friction=0.03, name="balle"):
		
 		boule.Boule.__init__(self, m, r, p0, v0, a0, friction, bounce_friction, name)
 		self.type = "balle"
 		self.img = sf.Image()
 		self.img.LoadFromFile("img/volleyball.png")
 		self.sprite = sf.Sprite(self.img)
