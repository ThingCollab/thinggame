import pygame, urllib, cStringIO
from pygame import *
from hero import *
from tile import *
from enemy import *
from projectile import *

allGroup = pygame.sprite.Group()
heroGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
tileGroup = pygame.sprite.Group()
obstacleGroup = pygame.sprite.Group()
waterGroup = pygame.sprite.Group()
lavaGroup = pygame.sprite.Group()
projectileGroup = pygame.sprite.Group()

hero.groups = allGroup, heroGroup
obstacle.groups = allGroup, tileGroup, obstacleGroup
water.groups = allGroup, tileGroup, waterGroup
lava.groups = allGroup, tileGroup, lavaGroup
enemy.groups = allGroup, enemyGroup
projectile.groups = allGroup, projectileGroup

class level:
	
	def __init__(self, tileDim):
		self.levelSurface = pygame.display.set_mode((736, 480))
		myHero = hero((128,64))
		myEnemies = []
		myEnemy = enemy((64,64))
		myEnemies.append(myEnemy);
		myEnemy = enemy((256,64))
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
					p = obstacle((x, y))
					tiles.append(p)
				elif column == "W":
					p = water((x,y))
					tiles.append(p)
				elif column == "L":
					p = lava((x,y))
					tiles.append(p)
				x += 32
			y += 32
			x = 0

	def update(self):
		self.levelSurface.fill((63,127,255));
		heroGroup.update(obstacleGroup, waterGroup, lavaGroup, enemyGroup, projectileGroup)
		enemyGroup.update(obstacleGroup)
		projectileGroup.update(obstacleGroup)
		tileGroup.update()
		enemyGroup.draw(self.levelSurface)
		heroGroup.draw(self.levelSurface)
		tileGroup.draw(self.levelSurface)
		pygame.display.flip()

