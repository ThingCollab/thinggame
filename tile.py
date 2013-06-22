import pygame, urllib, cStringIO
from pygame import *

class obstacle(pygame.sprite.Sprite):
	width = 32
	height = 32
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.pos = startpos
		self.image = pygame.Surface((self.width,self.height))
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.topleft = self.pos

class water(pygame.sprite.Sprite):
	width = 32
	height = 32
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.pos = startpos
		self.image = pygame.Surface((self.width,self.height))
		self.image.fill((0,0,255))
		self.image.set_alpha(127)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.topleft = self.pos

class lava(pygame.sprite.Sprite):
	width = 32
	height = 32
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.pos = startpos
		self.image = pygame.Surface((self.width,self.height))
		self.image.fill((255,127,0))
		self.image.set_alpha(239)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.topleft = self.pos
