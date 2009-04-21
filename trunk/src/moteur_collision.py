# coding=UTF-8
from PySFML import sf
import cmath

class moteur_collision :

	
	def __init__(self, carte, w):
		self.pile_balles = []
		self.coeff = 20
		self.carte = carte
		self.w = w
	
	def ajouter_objet(self, obj):
		self.pile_balles.append(obj)

	def supprimer_objet(self, obj):
		self.pile_balles.remove(obj)

	def update(self):
		for a in self.pile_balles :
			if not self.estDansLaMap(a.getx(), a.gety()):
				a.setpos(100,100)

		for i in range(len(self.pile_balles)):
		 	self.pile_balles[i].Move(self.w)
		 	
		 	if self.estDansLaMap(self.pile_balles[i].getx(), self.pile_balles[i].gety()) :
				if self.carte.RoughlyCheckCollision(self.pile_balles[i].p.real+self.pile_balles[i].r, self.pile_balles[i].p.imag+self.pile_balles[i].r, self.pile_balles[i].r) and self.pile_balles[i].getType() != "personnage" and self.pile_balles[i].p.imag >= 0: # Dￃﾩtection de collision approximative
					collision_data = self.carte.CheckCollision(self.pile_balles[i].p.real+self.pile_balles[i].r, self.pile_balles[i].p.imag+self.pile_balles[i].r, self.pile_balles[i].r) # Dￃﾩtection prￃﾩcise
					if collision_data != 42:
						self.pile_balles[i].Bounce(collision_data)
			elif self.pile_balles[i].p.imag <= 0 : # balle au dessus de l'écran
				if self.pile_balles[i].p.real <= 0 or self.pile_balles[i].p.real >= self.carte.getW(): # contacte avec un bord (x)
					self.pile_balles[i].v = complex(-self.pile_balles[i].v.real, self.pile_balles[i].v.imag)
				
#			if self.pile_balles[i].getType() == "personnage" :
			for j in range(i+1, len(self.pile_balles)):
				if self.estDansLaMap(self.pile_balles[j].getx(), self.pile_balles[j].gety()) :
					self.pile_balles[i].CheckCollision(self.pile_balles[j]) # Collision avec les autres balles
#					else :
#						print "Hors map!"
#			else :
#				for j in range(i+1, len(self.pile_balles)):
#					if self.pile_balles[j].getType() == "balle" and self.estDansLaMap(self.pile_balles[j].getx(), self.pile_balles[j].gety()) :
#						self.pile_balles[i].CheckCollision(self.pile_balles[j]) # Collision avec les autres balles
#					else:
#						print "Hors map!"
	#			for j in range(0, len(self.pile_joueurs)):
	#				self.pile_balles[i].CheckCollision(self.pile_joueurs[j]) # Collision avec les autres balles		
	#	        for b in self.pile_balles :
	#				for j in self.pile_joueurs :
	#					if self.portee(b, j) :
	#						b.set_velx((b.getx()-j.getx())*self.coeff)
	#						b.set_vely((b.gety()-j.gety())*self.coeff)
	
#	def collision(self, c1, c2):
#		if c1.getimpact() == 0 :
#			if((abs(c1.getx()+c1.getRadius()-c2.getx()-c2.getRadius()))<= c1.getRadius()+c2.getRadius()):
#			    if((abs(c1.gety()+c1.getRadius()-c2.gety()-c2.getRadius()))<= c1.getRadius()+c2.getRadius()):
#				diff_x = c1.getx()+c1.getRadius()-c2.getx()-c2.getRadius()
#				dir_x = -1
#				if diff_x < 0 :
#					diff_x = diff_x * -1
#					dir_x = 1
#				diff_y = c1.gety()+c1.getRadius()-c2.gety()-c2.getRadius()
#				dir_y = -1
#				if diff_y < 0 :
#					diff_y = diff_y * -1
#					dir_y = 1
#				
#				if self.force > 0 :
#					c2.set_vely(diff_y*dir_y/2.0*1.3)
#					c2.set_velx(diff_x*dir_x/10.0*1.3)
#				else :
#					c2.set_vely(diff_y*dir_y/2.0)
#					c2.set_velx(diff_x*dir_x/10.0)
#				#print "vely =",diff_y*dir_y/1.1
#				#print "velx =",diff_x*dir_x/10.0
#				c1.setimpact(20)
#				self.energie_plus()
#
#	def obstacle(self,obs):
#		res = obs.collision(self.getx(), self.gety(), self.getRadius())
#	        if(res != 0) :
#			if self.x+self.getRadius() < obs.getx():
#				self.setX(self.getx()-1)
#			else :
#				self.setX(self.getx()+1)
#			self.setXdir(0)
#	def collision(self, x, y , r) : # 1 par la droite, 2 par la gauche, 3 par dessous, 4 par dessus
#		if(x > self.left - r*2 and x < self.right and y > self.top-2*r and y < self.bottom):
#			if(x+2*r+2 >=self.left and x < self.right) :
#				return 1
#			elif (x <= self.right and x > self.left) :
#				return 2
#			elif (y <= self.bottom and y > self.top) :
#				return 3
#			elif (y+2*r+2 >=self.top and y < self.bottom) :
#				return 3
#			else :
#				return 0
#		else:
#			return 0		

	def portee(self, a, b):
		return abs(a.getx()+a.getRadius()-b.getx()-b.getRadius())<= a.getRadius()+b.getRadius() and abs(a.gety()+a.getRadius()-b.gety()-b.getRadius()) <= a.getRadius()+b.getRadius()
	def estDansLaMap(self, x, y):
		return (x>=0 and y>=0 and x <= self.carte.getW() and y <= self.carte.getH())

	def getSprite(self):
		l=[]
        	for a in self.pile_balles:
        		l.append(a.getSprite())
	        return l
	
	def nb_p(self) :
		return len(self.pile_balles)
