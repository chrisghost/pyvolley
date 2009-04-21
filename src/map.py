# coding=UTF-8

from PySFML import sf

import math

class map:

	def __init__(self):
		self.mask = sf.Image()
		self.mask.LoadFromFile("img/map.png")
		self.sprite = sf.Sprite(self.mask)
		
	def getW(self):
		return self.map_x*self.rough_map_tile_size
	def getH(self):
		return self.map_y*self.rough_map_tile_size

	def GetSquareState(self, tile_size, x, y):
		# S'il y a une seul pixel opaque dans le carré de taille tile_size et de coin supérieur gauche
		# (x, y), cette fonction renvoie True, et sinon False.
		for j in range(tile_size):
			for i in range(tile_size):
				if self.mask.GetPixel(x+i, y+j).a >= 125:
					return True
		return False

	def GenerateRoughMap(self, tile_size):
		# Génère une carte approximative, à tile_size pixels près
		width, height = self.mask.GetWidth()/tile_size, self.mask.GetHeight()/tile_size
		self.map_x, self.map_y = width, height
		self.rough_map = []
		self.rough_map_tile_size = tile_size
		for j in range(height):
			line = []
			for i in range(width):
				line.append(self.GetSquareState(tile_size, tile_size*i, tile_size*j))
			self.rough_map.append(line)

	def RoughlyCheckCollision(self, x, y, r):
		# Fait une détection approximative de collision
		if y <= 0 :
			if y < -500 :
				return True
			return False
		
		start_x, start_y = int((x-r)/self.rough_map_tile_size), int((y-r)/self.rough_map_tile_size)
		end_x, end_y = int((x+r)/self.rough_map_tile_size)+1, int((y+r)/self.rough_map_tile_size)+1
		
		if start_x < 0 or start_y < 0 or end_x > len(self.rough_map[0]) or end_y >  len(self.rough_map):
		      return True
		     
		
		for j in range(start_y, end_y):
			for i in range(start_x, end_x):
				if self.rough_map[j][i]:
					return True
		return False

	def IsOpaque(self, x, y):
		
		if round(x) < 0 or round(x) > self.map_x*self.rough_map_tile_size or round(y) < 0 or round(y) > self.map_y*self.rough_map_tile_size :
#			print "Erreur coordonnées"
#			print round(x)
#			print round(y)
#			print "map:"
#			print self.map_x
#			print self.map_y
			return False
			
		x, y = int(round(x)), int(round(y))
		return (self.mask.GetPixel(x, y).a >= 125)
	
	def IsZoneOpaque(self,x_start,y_start,x_end,y_end):
		opaque = False
		i=x_start
		j=y_start
		while not opaque  and j < y_end:
			while i < x_end and not opaque :
				opaque = self.IsOpaque(i, j)
				i+=1
			j+=1
			i=x_start
		return opaque

	def CheckCollision(self, x, y, r):
		# Vérifie si le cercle de centre (x, y) et de rayon r est en collision avec le bord.
		# Connaissant les deux points d'intersection entre le cercle et la courbe de la carte,
		# on peut connaitre le point médian de collision (celui qui sera utilisé pour les calculs)
		# nb_points = Nombre de points de test.
		# Plus il est élevé, meilleure est la précision du calcul du point de collision.
		nb_points = 32

		theta0 = nb_points+1
		if self.IsOpaque(x+r, y):
			theta0 = 0
			while self.IsOpaque(x + r*math.cos(2*math.pi*theta0/nb_points), y + r*math.sin(2*math.pi*theta0/nb_points)) and theta0 > - nb_points:
				theta0 = theta0 - 1
		for theta in range(0, nb_points):
			nx, ny = x + r*math.cos(2*math.pi*theta/nb_points), y + r*math.sin(2*math.pi*theta/nb_points)
			if theta0 == nb_points+1:
				if self.IsOpaque(nx, ny): # premier point de contact trouvé
					theta0 = theta-1
			else:
				if not self.IsOpaque(nx, ny): # deuxième point de contact trouvé
					angle_median = 2*math.pi*(theta0 + theta)/(2*nb_points)
					# (px, py) est le vecteur de pénétration du cercle dans la courbe
					# si on translate le cercle de ce vecteur, le cercle n'est plus en
					# contact avec la courbe.
					# On aurait pu effectuer un calcul direct, mais c'est foireux si
					# nb_points est trop petit ou si la collision a lieu avec un pic.
					px0, py0 = x + r*math.cos(angle_median), y + r*math.sin(angle_median)
					px, py = px0, py0
					while self.IsOpaque(px, py):
						px = px + math.cos(math.pi + angle_median)
						py = py + math.sin(math.pi + angle_median)
					return (angle_median, complex(px - px0, py - py0))
		return 42 # pas de collision

