from PySFML import sf

class anim:	

	def __init__(self,s,intervale_subrect,x,y,posx,posy,position_depart):
		self.sprite = s
		self.intervale = intervale_subrect
		self.x = x
		self.y = y
		self.posx = posx
		self.posy = posy
		self.sprite.SetX(self.posx)
		self.sprite.SetY(self.posy)
		self.sprite.SetSubRect(sf.IntRect(0,0,self.intervale,self.y))
		self.position = position_depart

	def next(self) :
		self.position = self.position + 1
		if self.position == self.x/self.intervale:
			self.position = 0
		self.sprite.SetSubRect(sf.IntRect(self.position * self.intervale,0,self.position * self.intervale + self.intervale,self.y))

	def getSprite(self) :
		return self.sprite

	def addX(self,x) :
		self.posx = self.posx + x
		self.sprite.SetX(self.posx)
	def getX(self):
		return self.posx
		
	def setX(self,x):
		self.sprite.SetX(x)
	def setY(self,y):
		self.sprite.SetY(y)
	def getSizeX(self):
		return self.x
	def getSizeY(self):
		return self.y
