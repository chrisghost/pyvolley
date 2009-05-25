# coding=UTF-8
from PySFML import sf
import boule
import pers
import ball
import obstacle
import moteur_particule
import moteur_collision
import moteur_control
import map

class jeu:
    fond = sf.Image()
    back = sf.Sprite(fond)
    state = True
    carte = map.map()
    carte.GenerateRoughMap(30)

    def __init__(self, window, ig):
        self.window = window
        self.clock = sf.Clock()
	self.ig = ig
        
        print "Initialisation Gestionnaire de particules"
        self.moteur_p = moteur_particule.moteur_particule(ig)
        print "Création des joueurs"
        self.j1 = pers.Personnage(window, 100 + 500j, 10, 10, 1, "Marie", self.moteur_p, self.carte)
        print "Création des balles"
        self.ballon = ball.Ball(10, 25, 120 + 100j, 0 + 0j, 250j, 0.2, 0.04, "balle de fou")
        
        self.moteur_c = moteur_collision.moteur_collision(self.carte, self.window)
        self.moteur_c.ajouter_objet(self.j1)
        self.moteur_c.ajouter_objet(self.ballon)

        self.fond.LoadFromFile("img/hell.jpg")
        self.back = sf.Sprite(self.fond)
    
#        window.Draw(self.back)
        Input = self.window.GetInput()
        
        print "Chargement de la police"
        self.text = sf.String("", Size=20)
        self.text.SetPosition(20, 20)
        
        self.t1 = 1
        self.t2 = 2
        self.i=0
       
	self.control = moteur_control.moteur_control(self, window)
	self.control.addplayer(self.j1)

 
        while self.state and self.window.IsOpened():
            event = sf.Event()
            while self.window.GetEvent(event):
                if event.Type == sf.Event.Closed:
                    self.window.Close()
            
            self.iteration(Input)
            self.moteur_c.update()
            self.afficher_tout()
            self.control.Scan()
            ig.fps()
        
    def iteration(self, Input):
             self.j1.manage_keys(Input)
             pass
        
    def afficher_tout(self):
        self.window.Clear(sf.Color(0,0,0))  
        self.window.Draw(self.back)
        for sp1 in self.moteur_c.getSprite() :
            self.window.Draw(sp1)

        for sp in self.moteur_p.getSprite() :    
            self.window.Draw(sp)
  
	for sp in self.ig.getSprite() :    
		self.window.Draw(sp)

        self.window.Display()
