# coding=UTF-8
from PySFML import sf
from bmp import BitMap, Color

class ig :
	pile_elements = []
	pile_textes = []
	adr = []
	images = []
	
	last_fps_time = 0
	fps_l = []
	i=0
	text_size = 20
	
	def __init__(self, w,h, menu):
		self.w = w
		self.h = h
		self.clock = sf.Clock()
		self.id_text_fps = self.ajouter_texte(10,10, "fps : ")

		self.bmp = BitMap( w, h, Color(255,255,255))
		self.bmp.saveFile("button_map.bmp", False)
		
		self.mask = sf.Image()
		self.sprite = sf.Sprite(self.mask)
		
		self.menu = menu
	
	def ajouter_texte(self, x, y, texte):
	        text = sf.String(texte, Size= self.text_size)
        	text.SetColor(sf.Color(255, 255, 255))
        	text.SetPosition(x,y)
		self.pile_textes.append(text)
		return len(self.pile_textes)-1
		
	def maj_texte(self, id, texte):
		self.pile_textes[id].SetText(texte)

	def getSprite(self):
		l=[]
        	for a in self.pile_elements:
        		l.append(a)
        	for a in self.pile_textes:
        		l.append(a)
	        return l

	def fps(self) :
		a = self.clock.GetElapsedTime()
		if self.i < 50 :
	    		self.fps_l.append(1.0 / (a - self.last_fps_time))
	    	else :
	    		s = 0
	    		for pair in self.fps_l :
	    			s = s + pair
	    		self.maj_texte(self.id_text_fps, "fps : "+str( round(s/50,2)))
	    		self.i = 0
	    		self.fps_l = []
	    	
	    	self.last_fps_time = a
	    	self.i += 1

	def bouton(self, type, x, y, texte, func):
		# Definition des valeurs de func:
		# 1 - Nouveau Jeu
		# 2 - Options
		# 0 - Quitter
		
		if type == 1 :
			g = "img/bouton1g.png"
			c = "img/bouton1c.png"
			d = "img/bouton1d.png"

		largeur_c = len(texte)*self.text_size*(2.0/3.0)

		ig = sf.Image()
		ic = sf.Image()
		id = sf.Image()
		
		ig.LoadFromFile(g)
		ic.LoadFromFile(c)
		id.LoadFromFile(d)
		
		sg = sf.Sprite(ig)
		sc = sf.Sprite(ic)
		sd = sf.Sprite(id)
		
		sg.SetX(x)
		sc.SetX(x+10)
		sd.SetX(x+10+largeur_c)
		
		sc.SetSubRect(sf.IntRect(0,0,int(largeur_c),50))		
		
		sg.SetY(y)
		sc.SetY(y)
		sd.SetY(y)
		
		self.pile_elements.append(sg)
		self.pile_elements.append(sc)
		self.pile_elements.append(sd)
		
		self.ajouter_texte(x+10,y+10,texte)
		
		self.bmp.setPenColor(Color(func,255,255))
		self.bmp.drawRect(x,self.h-y,largeur_c+20, 50, True)
		self.bmp.saveFile("button_map.bmp", False)


	def execute(self, i):
		if i == 0 : # Quitter
			self.menu.setState(False)
		elif (i == 1) :# Nouveau jeu
			self.menu.setNext(i)
		elif i == 2 : # Options
			print "OPT"
		else :
			print "Nothing"

	def detect_collision(self, l):
		for i in l:
			if i[0] <= self.w and i[0] > 0 and i[1] <= self.h and i[1] > 1 :
				if self.GetColor(i[0],i[1]).r != 255:
					print self.GetColor(i[0],i[1]).r
					self.execute(self.GetColor(i[0],i[1]).r)
					
					
	def deleteAll(self):
		pile_elements = []
		pile_textes = []
		adr = []
		images = []
		
	def init_detect(self):
		self.mask = sf.Image()
		self.mask.LoadFromFile("button_map.bmp")
		self.sprite = sf.Sprite(self.mask)
	
	def GetColor(self, x, y):	
		x, y = int(round(x)), int(round(y))
		return self.mask.GetPixel(x, y)
