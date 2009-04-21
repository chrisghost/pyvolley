# coding=UTF-8
from PySFML import sf
import cmath

class Boule:


	def __init__(self, m, r, p0=complex(200, 300), v0=complex(0, 122), a0=complex(0, 0.15), friction=0.5, bounce_friction=0.03, name="balle"):
		self.a = a0 # acceleration initiale = gravitée (attention, elle n'est pas divisée par m dans les calculs)
	        self.v = v0 # vitesse initiale
	        self.p = p0 # position initiale
	        self.friction = friction # frottements avec l'air
	        self.bounce_friction = bounce_friction # Pourcentage d'énergie cinétique perdue à chaque collision
	        # clock et old_time_value servent à calculer l'écart de temps entre deux calculs
	        self.old_time_value = 0
	        self.r = r # rayon de la balle
	        self.m = m # masse de la balle (utilisée uniquement pour les collisions avec un autre ball)
	        self.name = name
	        self.clock = sf.Clock()
	        self.img = sf.Image()
	        self.sprite = sf.Sprite(self.img)
	        self.type = ""

	def Move(self):
		# Temps écoulé depuis le dernier calcul
		t = self.clock.GetElapsedTime()
		self.delta = t - self.old_time_value
		self.old_time_value = t

		# Mise à jour de la vitesse
		self.v = self.v * (1-self.delta*self.friction) + self.a * self.delta
		# Mise à jour de la position
		self.p += self.v * self.delta

		self.sprite.SetPosition(self.p.real, self.p.imag)

#		self.delta = w.GetFrameTime()

#		i = 0
#        if self.v.real > self.vmax.real :
#            self.v = complex(self.vmax.real, self.v.imag)
#            i = 1
#        elif self.v.real < -self.vmax.real :
#            self.v = complex(-self.vmax.real, self.v.imag)
#            i = 1
#        if self.v.imag > self.vmax.imag :
#            self.v = complex(self.v.real, self.vmax.imag)
#            i = 1
#        elif self.v.imag < -self.vmax.imag :
#            self.v = complex(self.v.real, -self.vmax.imag)
#            i = 1


	def GetVAngle(self):
		# Je ne m'en sert pas ici mais ça peut être utile :)
		if self.v == 0j:
			return 0
		else:
			return cmath.log(self.v).imag

	def Bounce(self, collision_data):
		# Il semblerait que l'objet vienne de cogner un mur.
		angle, delta_p = collision_data
		# collision_data[0] contient l'angle de la normale de l'obstacle.
		self.v = - (1 - self.bounce_friction) * self.v.conjugate() * cmath.exp(2j*angle)
		# Corriger la position pour ne pas rentrer à l'intérieur du mur
		self.p += delta_p

	def CheckCollision(self, ball):
		# Collision avec un autre objet ball
		if abs(ball.p - self.p) < self.r + ball.r: # uh-oh, collision
			# Axe entre le centre des deux balles (normale de la collision)
			n = (ball.p - self.p) / abs(ball.p - self.p)
			vap = (self.v / n).real # On projète la vitesse sur la normale
			van = (-1j * self.v / n).real # On projète la vitesse sur la perpendiculaire à la normale
			# Ensuite on fait pareil pour la vitesse de ball
			vbp = (ball.v / n).real
			vbn = (- 1j * ball.v / n).real

			# Maintenant qu'on a projeté la vitesse dans le repère de la normale et de sa perpendiculaire,
			# le problème est le même que dans le cas d'une seule dimension.
			# On calcule les nouvelles coordonnées de la vitesse après collision dans le nouveau repère,
			# en prenant compte des masses des deux objets.
			s = (self.m+ball.m)
			vap2 = ((self.m-(1-self.bounce_friction)*ball.m)/s)*vap + ((2-self.bounce_friction)*ball.m/s)*vbp
			vbp2 = ((2-ball.bounce_friction)*self.m/s)*vap + ((ball.m-(1-ball.bounce_friction)*self.m)/s)*vbp
			# Il ne reste plus qu'à revenir dans notre repère bien aimé.
			self.v = vap2*n + van*n*1j
			ball.v = vbp2*n + vbn*n*1j

			# Pour éviter que les deux balles se rentrent dedans, on corrige la position proportionnellement à
			# la masse relative (le plus léger bouge plus)
			d = self.r + ball.r - abs(ball.p - self.p) + 1
			self.p -= n*d*ball.m/s
			ball.p += n*d*self.m/s

			
	def getSprite(self):
		return self.sprite
	def getSprite_p(self):
		return self.sprite_p
	def setpos(self,x,y):
		self.p = complex(x,y)


	def getSprite(self):
		return self.sprite
	def getType(self):
		return self.type
	def getName(self):
		return self.name
	def getx(self) :
		return self.p.real
	def gety(self) :
		return self.p.imag
	def getRadius(self):
		return self.r
	def setpos(self,x,y):
		self.p = complex(x,y)

