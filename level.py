import pygame, urllib, cStringIO
from pygame import *
from hero import *
from obstacle import *
from enemy import *
from projectile import *

allGroup = pygame.sprite.Group()
heroGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
obstacleGroup = pygame.sprite.Group()
projectileGroup = pygame.sprite.Group()

hero.groups = allGroup, heroGroup
obstacle.groups = allGroup, obstacleGroup
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
		"O  OOOOO  OOO  O   O  O",
		"O    O   O   O O  O   O",
		"O    O   O   O O O    O",
		"O    O    OOO  OO     O",
		"O    O       O O O    O",
		"O    O       O O  O   O",
		"O    O    OOO  O   O  O",
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
				x += 32
			y += 32
			x = 0

	def update(self):
		self.levelSurface.fill((63,127,255));
		heroGroup.update(obstacleGroup, enemyGroup, projectileGroup)
		enemyGroup.update(obstacleGroup)
		projectileGroup.update(obstacleGroup)
		obstacleGroup.update()
		allGroup.draw(self.levelSurface)
		pygame.display.flip()

