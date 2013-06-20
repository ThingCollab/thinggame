import pygame, urllib, cStringIO
from pygame import *
from hero import *
from obstacle import *
from enemy import *

allgroup = pygame.sprite.Group()
herogroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
obstacleGroup = pygame.sprite.Group()
hero.groups = allgroup, herogroup
obstacle.groups = allgroup, obstacleGroup
enemy.groups = allgroup, enemyGroup

class level:
	
	def __init__(self, tileDim):
		self.levelSurface = pygame.display.set_mode((720, 480))
		myHero = hero((64,64))
		myEnemy = enemy((64,64))
		tiles = []
		levelArray = [
		"OOOOOOOOOOOOOOOOOOOOO",
		"O                   O",
		"O OOOOO  OOO  O   O O",
		"O   O   O   O O  O  O",
		"O   O   O   O O O   O",
		"O   O    OOO  OO    O",
		"O   O       O O O   O",
		"O   O       O O  O  O",
		"O   O    OOO  O   O O",
		"O                   O",
		"OOOOOOOOOOOOOOOOOOOOO",]
		x = y = 0
		for row in levelArray:
			for column in row:
				if column == "O":
					p = obstacle((x, y))
					tiles.append(p)
				x += 32
			y += 32
			x = 0
#		myObstacle = obstacle([self.levelSurface.get_size()[0]/2-smiley.get_size()[0]*0.5,self.levelSurface.get_size()[1]-72])

	def update(self):
		self.levelSurface.fill((63,127,255));
		herogroup.update(obstacleGroup, enemyGroup)
		enemyGroup.update(obstacleGroup)
		obstacleGroup.update()
		allgroup.draw(self.levelSurface)
		pygame.display.flip()

