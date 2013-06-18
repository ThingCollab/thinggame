import pygame, urllib, cStringIO
from pygame import *

screen = pygame.display.set_mode((640, 480))

file = cStringIO.StringIO(urllib.urlopen("http://images.wikia.com/smileyofawesome/images/b/bc/Wiki.png").read())
smiley = pygame.transform.smoothscale(pygame.image.load(file), (32,32))

bounds = [[0,0],[screen.get_size()[0]-smiley.get_size()[0],screen.get_size()[1]-smiley.get_size()[1]]]

class hero(pygame.sprite.Sprite):
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.vel = [0,0]
		self.image = smiley
		self.rect = self.image.get_rect()
		self.rect.topleft = startpos
		self.ground = False
	def update(self, obstacles):
		acc = [0,0]
		jump = 0
		if pygame.key.get_pressed()[K_SPACE]:
			if self.ground: self.vel[1] -= 15
		self.vel[0] = 0
		if pygame.key.get_pressed()[K_RIGHT]:
			self.vel[0] =  5
		if pygame.key.get_pressed()[K_LEFT]:
			self.vel[0] = -5
		if not self.ground:
			self.vel[1] += 1;
		self.rect.left += self.vel[0]
		self.collide(self.vel[0], 0, obstacles)
		self.rect.top += self.vel[1]
		self.ground = False
		self.collide(0, self.vel[1], obstacles)
		
	def collide(self, velX, velY, obstacles):
		for obstacle in obstacles:
			if sprite.collide_rect(self, obstacle):
				if velX > 0: self.rect.right = obstacle.rect.left
				if velX < 0: self.rect.left = obstacle.rect.right
				if velY > 0:
					self.rect.bottom = obstacle.rect.top
					self.ground = True
					self.vel[1] = 0
				if velY < 0: self.rect.top = obstacle.rect.bottom

