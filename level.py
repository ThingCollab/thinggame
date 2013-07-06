import pygame, urllib, cStringIO
from pygame import *
from tile import *
from entity import *
from projectile import *
from spritesheet import *

class level:
	def __init__(self):
		self.state = "Level"
		self.allGroup = pygame.sprite.Group()
		self.entityGroup = pygame.sprite.Group()
		self.tileGroup = pygame.sprite.Group()
		self.obstacleGroup = pygame.sprite.Group()
		self.waterGroup = pygame.sprite.Group()
		self.lavaGroup = pygame.sprite.Group()
		self.projectileGroup = pygame.sprite.Group()
		self.tileSet = spritesheet("Basic Tileset.png",32)
		Tile.groups = self.allGroup, self.tileGroup
		entity.groups = self.allGroup, self.entityGroup
		projectile.groups = self.allGroup, self.projectileGroup
		self.levelSurface = pygame.display.set_mode((736, 480))
	def load(self):
		entities = []
		tiles = []
		levelArray = [
					  "OOOOOOOOOOOOOOOOOOOOOOO",
					  "O                     O",
					  "O                     O",
					  "O  0                  O",
					  "O  OOOOO  WWW  L   L  O",
					  "O    O   W   W L  L   O",
					  "O    O   W   W L L    O",
					  "O    O    WWW  LL     O",
					  "O    O       W L L    O",
					  "O    O       W L  L   O",
					  "O    O    WWW  L   L  O",
					  "O                     O",
					  "O                     O",
					  "O  2  2   2  2      2 O",
					  "OOOOOOOOOOOOOOOOOOOOOOO",]
		x = y = 0
		for row in levelArray:
			for column in row:
				if column == "O": tiles.append(Tile((x, y), 1, 1, self.tileSet))
				elif column == "W": tiles.append(Tile((x, y), 2, 2, self.tileSet))
				elif column == "L": tiles.append(Tile((x, y), 3, 3, self.tileSet))
				elif column == "l": tiles.append(Tile((x, y), 4, 4, self.tileSet))
				elif column == "0": entities.append(entity((x,y),0))
				elif column == "2": entities.append(entity((x,y),2))
				x += 32
			y += 32
			x = 0
	def unload(self):
		for item in self.allGroup: item.kill()
	def update(self):
		self.levelSurface.fill((63,127,255));
		self.entityGroup.update(self.tileGroup, self.entityGroup, self.projectileGroup)
		self.projectileGroup.update(self.tileGroup)
		self.tileGroup.update()
		self.projectileGroup.draw(self.levelSurface)
		self.entityGroup.draw(self.levelSurface)
		self.tileGroup.draw(self.levelSurface)
		pygame.display.flip()
	def writeLevel(self):
		print "TILES"
		for tile in self.tileGroup:
			print str(tile.type)+"\t"+str(tile.pos)+"\t"
		for entity in self.entityGroup:
			print str(entity.type)+"\t"+str(entity.pos)+"\t"+str(entity.vel)+"\t"+str(entity.health)
		for projectile in self.projectileGroup:
			print str(projectile.type)+"\t"+str(projectile.pos)+"\t"+str(projectile.vel)+"\t"+str(projectile.targetTypes)
