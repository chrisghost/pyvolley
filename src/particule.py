import anim
import math

class particule :
	m_vie = 0
	m_vitesse = 0.0
	m_angle = 0.0

	m_coordonnee_x = 0
	m_coordonnee_y = 0

	m_type = 0 # 10 = feu
	animation = 0
	
	time = 0
	
	def __init__(self, vie, vit, angle, x, y, type_p, intervale_subrect,x_t,y_t,position_depart,s):
		self.m_vie = vie
		self.m_vitesse = vit
		self.m_angle = angle
		self.m_coordonnee_x = x
		self.m_coordonnee_y = y
		self.m_type = type_p
		self.animation = anim.anim(s,intervale_subrect,x_t,y_t,x,y,position_depart)

	def update(self):
		self.time = self.time + 1
		if self.time == 2 :
			self.animation.next()
			self.time = 0
		self.m_coordonnee_x = self.m_coordonnee_x + (math.cos(self.m_angle*(3.14/180)))*self.m_vitesse
		self.m_coordonnee_y = self.m_coordonnee_y + (math.sin(self.m_angle*(3.14/180)))*self.m_vitesse
		self.animation.setX(self.m_coordonnee_x)
		self.animation.setY(self.m_coordonnee_y)
		self.m_vie -= 1
	def getSprite(self):
		return self.animation.getSprite()
		
	def getVie(self) :
		return self.m_vie
	def getType(self) :
		return self.m_type
	def getX(self):
		return self.m_coordonnee_x
	def getY(self):
		return self.m_coordonnee_y
	def getSizeX(self):
		return self.animation.getSizeX()
	def getSizeY(self):
		return self.animation.getSizeY()
