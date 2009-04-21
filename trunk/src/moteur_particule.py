import particule
import random
import cmath
from PySFML import sf

class moteur_particule :
	pile_particule = []
	adr = []
	images = []
	
	def __init__(self, ig):
		self.ig = ig
		
	def deleteAll(self):
		for a in self.pile_particule :
			self.pile_particule.remove(a)
		for a in self.adr :
			self.adr.remove(a)
		for a in self.images :
			self.images.remove(a)
	
	def ajouter_particule(self,vie, vit, angle, x, y, type_p, adr_img,intervale_subrect,x_t,y_t,position_depart):
		b = "nul"
		for a in self.adr :
			if a == adr_img :
				b = a
		if b != "nul" :
			idx = self.adr.index(b)
		else :
			idx = len(self.adr)
			i = sf.Image()
			i.LoadFromFile(adr_img)
			self.adr.append(adr_img)
			self.images.append(i)
			
		s = sf.Sprite(self.images[idx])
		self.pile_particule.append(particule.particule(vie, vit, angle, x, y, type_p, intervale_subrect,x_t,y_t,position_depart, s))

	def supprimer_particule_morte(self):
		l=[]
		list = ["img/fireball.png" ,"img/fireball_r.png" ,"img/fireball_b.png"]
		for a in self.pile_particule:
			if a.getVie() <= 0 :
				if a.getType() >= 20 and a.getType() <= 22: #boule de feu
					
					self.ajouter_particule(10, 5, random.randint(0,359), a.getX(), a.getY(), 19, list[a.getType()-20] , 50,50,50,0)
					self.ajouter_particule(10, 5, random.randint(0,359), a.getX(), a.getY(), 19, list[a.getType()-20] , 50,50,50,0)
					self.ajouter_particule(10, 5, random.randint(0,359), a.getX(), a.getY(), 19, list[a.getType()-20] , 50,50,50,0)
					l.append([a.getX(),a.getY()])
				
				self.checkCollisions(l)
				self.ig.detect_collision(l)
				self.pile_particule.remove(a)
		return l
	
	def checkCollisions(self, l):
		for a in l :
			for b in self.pile_particule:
				if abs(a[0] - b.getX()) <= 20 and abs(a[1] - b.getY()) <= 20 and b.getType() == 31 : #ennemi num 1
				    self.ajouter_particule(10, 0.01, 0, b.getX(), b.getY(), 1, "img/ennemi_1_mort.png" , 50,50,50,0)
				    self.pile_particule.remove(b)

	def update_particule(self):
	        for a in self.pile_particule:
	        	a.update()
		self.checkCollisions(self.supprimer_particule_morte())
		
	def collision(self,x,y,r):
		for a in self.pile_particule :
			pass

	def getSprite(self):
		l=[]
        	for a in self.pile_particule:
        		l.append(a.getSprite())
	        return l
	
	def nb_p(self) :
		return len(self.pile_particule)
		
	def new_meteor(self, x, y, width):
		rd = random.randint(0, width)
		
		vie = 20.0
		cote_plat = abs(rd - x)
		cote_droit = y
		oblique = cmath.sqrt(cote_plat * cote_plat + cote_droit * cote_droit)
		vitesse = oblique / vie
		
		alpha = (cmath.acos(cote_plat / oblique) * 180 / cmath.pi)
		
		if rd < x :
		    angle = alpha
		else :
		    angle = 180 - alpha
		    
		nb = random.randint(2, 15)
		
		list = ["img/ball_flammes.png" ,"img/fireball_r.png" ,"img/fireball_b.png"]
		
		color = random.randint(0, 2)
		
		for i in range(0,nb) :
		    pos = random.randint(-10, 10)
		    self.ajouter_particule(vie, vitesse.real, angle.real, rd + pos -25, -25, 20+color, list[color] , 50, 50, 50, 0)
