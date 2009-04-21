import particule
import random
import anim
from PySFML import sf

class moteur_ennemis :
	pile_ennemis = []
	pile_ennemis_morts = []
	adr = []
	images = []
	
	def __init__(self):
		pass
	
	def ajouter_ennemi(self,vit, angle, x, y, adr_img, adr_img2, intervale_subrect,x_t,y_t,position_depart):
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
		
		b = "nul"
		for a in self.adr :
			if a == adr_img2 :
				b = a
		if b != "nul" :
			idx = self.adr.index(b)
		else :
			idx = len(self.adr)
			i = sf.Image()
			i.LoadFromFile(adr_img2)
			self.adr.append(adr_img2)
			self.images.append(i)
			
		s2 = sf.Sprite(self.images[idx])
		self.pile_particule.append(anim.anim(s,intervale_subrect,x_t,y_t,posx,posy,position_depart))
		self.pile_ennemis_morts.append(s2)

	def supprimer_ennemi_fini(self):
		for a in self.pile_ennemis :
			if a.getVie() <= 0 :
				self.pile_ennemis.remove(a)

	def update_particule(self):
	        for a in self.pile_particule:
	        	a.update()
		a = self.supprimer_particule_morte()
		return a
		
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
