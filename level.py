import pygame, urllib, cStringIO
from pygame import *
from tile import *
from entity import *
from projectile import *

allGroup = pygame.sprite.Group()
entityGroup = pygame.sprite.Group()
tileGroup = pygame.sprite.Group()
obstacleGroup = pygame.sprite.Group()
waterGroup = pygame.sprite.Group()
lavaGroup = pygame.sprite.Group()
projectileGroup = pygame.sprite.Group()

tile.groups = allGroup, tileGroup
entity.groups = allGroup, entityGroup
projectile.groups = allGroup, projectileGroup

class level:
	
	def __init__(self, tileDim):
		self.levelSurface = pygame.display.set_mode((736, 480))
		myHero = entity((128,64),0)
		myEnemies = []
		myEnemy = entity((64,64),1)
		myEnemies.append(myEnemy);
		myEnemy = entity((256,64),1)
		myEnemies.append(myEnemy);

		tiles = []
		levelArray = [
		"OOOOOOOOOOOOOOOOOOOOOOO",
		"O                     O",
		"O                     O",
		"O                     O",
		"O  OOOOO  WWW  L   L  O",
		"O    O   W   W L  L   O",
		"O    O   W   W L L    O",
		"O    O    WWW  LL     O",
		"O    O       W L L    O",
		"O    O       W L  L   O",
		"O    O    WWW  L   L  O",
		"O                     O",
		"O                     O",
		"O                     O",
		"OOOOOOOOOOOOOOOOOOOOOOO",]
		x = y = 0
		for row in levelArray:
			for column in row:
				if column == "O":
					p = tile((x, y),1)
					tiles.append(p)
				elif column == "W":
					p = tile((x, y),2)
					tiles.append(p)
				elif column == "L":
					p = tile((x, y),3)
					tiles.append(p)
				x += 32
			y += 32
			x = 0

	def update(self):
		self.levelSurface.fill((63,127,255));
		entityGroup.update(tileGroup, entityGroup, projectileGroup)
		projectileGroup.update(tileGroup)
		tileGroup.update()
		projectileGroup.draw(self.levelSurface)
		entityGroup.draw(self.levelSurface)
		tileGroup.draw(self.levelSurface)
		pygame.display.flip()

