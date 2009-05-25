from PySFML import sf
import moteur_particule
import random
import cmath
import ig
import jeu
import kinput
import moteur_control

class menu:
#    window = sf.RenderWindow(sf.VideoMode(800, 600), "pyVolley")
    fond = sf.Image()
    back = sf.Sprite(fond)
    
    ipointeur = sf.Image()
    pointeur = sf.Sprite(ipointeur)
    next = -1
#    arme = sf.Image()
#    arme2 = sf.Image()
#    arme_sp2 = sf.Sprite(arme2)
#    arme_sp = sf.Sprite(arme)
    state = True
    
    def none(self, a):
    	print "NONE"
    
    def setNext(self, s):
    	self.next = s
    def setState(self, s):
    	self.state = s
    
    def Next(self):
    	if self.next == 1 :
    		self.moteur_p.deleteAll()
		self.ig.deleteAll()
    		jeu.jeu(self.window, self.ig)
    	elif self.next == 2 :
    		#Options
            pass
        else :
        	pass


    def __init__(self, window):
        
        print "Initialisation de l'interface graphique"
        self.ig = ig.ig(800,600, self)
        
        print "Initialisation du menu"
        
        self.window = window
        self.fond.LoadFromFile("img/menu.jpg")
        self.back = sf.Sprite(self.fond)
        
        self.ipointeur.LoadFromFile("img/pointeur.png")
        self.pointeur = sf.Sprite(self.ipointeur)

        Input = self.window.GetInput()
        
        self.moteur_p = moteur_particule.moteur_particule(self.ig)
        
        self.ig.ajouter_texte(200,10, "pyVolley")
        self.ig.bouton(1, 10, 100, "Nouveau jeu", 1)
        self.ig.bouton(1, 10, 200, "Options", 2)
        self.ig.bouton(1, 10, 300, "Quitter", 0)
        self.ig.init_detect()
        
	self.control = moteur_control.moteur_control(self, window)
#   	 self.input = kinput.kInput(self.window)
#        self.input.AddEvent(sf.Event.KeyPressed, sf.Key.F15, self.none, (False))
#        self.input.AddEvent(sf.Event.KeyReleased, sf.Key.F15, self.none, (False))
#        self.input.AddEvent(sf.Event.MouseButtonPressed, sf.Mouse.Count, self.none, (False))
#        self.input.AddEvent(sf.Event.MouseButtonReleased, sf.Mouse.Left, self.none, (False))
        
# 	 self.input.AddEvent(sf.Event.KeyPressed, sf.Key.N, self.setNext, (1))
#        self.input.AddEvent(sf.Event.KeyPressed, sf.Key.Escape, self.setState, (False))
#        self.input.AddEvent(sf.Event.MouseButtonPressed, sf.Mouse.Left, self.moteur_p.new_meteor, ("_Mouse_X", "_Mouse_Y",800)) 
						
        while self.state :
        	
#	        	self.input.Scan()
			self.control.Scan()
			self.Next()

			a = self.moteur_p.update_particule()
			
			if random.randint(0, 1000) > 995 :
				self.moteur_p.ajouter_particule(1000, 2, 0, 0, random.randint(100, 500), 31, "img/ennemi_1.png" , 50, 50, 50, 0)
			
			event = sf.Event()
			while self.window.GetEvent(event):
				if event.Type == sf.Event.Closed:
					self.window.Close()

							
			self.ig.fps()
			
			self.pointeur.SetX(Input.GetMouseX()-self.ipointeur.GetWidth()/2)
			self.pointeur.SetY(Input.GetMouseY()-self.ipointeur.GetHeight()/2)
			
			self.window.Draw(self.back)
			for sp in self.moteur_p.getSprite() :    
				self.window.Draw(sp)

			for sp in self.ig.getSprite() :    
				self.window.Draw(sp)
				
			self.window.Draw(self.pointeur)

			self.window.Display()
