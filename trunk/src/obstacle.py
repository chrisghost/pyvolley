
class Obstacle :
	top=0
	left=0
	bottom=0
	right = 0

	def getType(self):
		return "obstacle"

	def __init__(self, t, l, b, r) :
		self.top = t
		self.left = l
		self.bottom = b
		self.right = r

	def collision(self, x, y , r) : # 1 par la droite, 2 par la gauche, 3 par dessous, 4 par dessus
		if(x > self.left - r*2 and x < self.right and y > self.top-2*r and y < self.bottom):
			if(x+2*r+2 >=self.left and x < self.right) :
				return 1
			elif (x <= self.right and x > self.left) :
				return 2
			elif (y <= self.bottom and y > self.top) :
				return 3
			elif (y+2*r+2 >=self.top and y < self.bottom) :
				return 3
			else :
				return 0
		else:
			return 0

	def getx(self) :
		return (self.left+self.right)/2
#    def filet(self,x, pos):
#	if pos == 1:
#		if self.x+self.getRadius()*2+self.vel_moving > x :
#			self.velx = 0
#			self.x = x-self.getRadius()*2-self.vel_moving
#	else :
#		if self.x-self.vel_moving < x :
#			self.velx = 0
#			self.x = x+self.vel_moving
