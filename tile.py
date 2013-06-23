import pygame, urllib, cStringIO
from pygame import *

class tile(pygame.sprite.Sprite):
	width = 32
	height = 32
	type = 0
#	Types:
#	0: Air
#	1: Obstacle
#	2: Water
#	3: Lava
	def __init__(self, startpos, starttype):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.pos = startpos
		self.type = starttype
		if not self.type == 0:
			self.image = pygame.Surface((self.width,self.height))
			self.rect = self.image.get_rect()
			if self.type == 2:
				self.image.fill((0,0,255))
				self.image.set_alpha(127)
			if self.type == 3:
				self.image.fill((255,127,0))
				self.image.set_alpha(239)
	def update(self):
		self.rect.topleft = self.pos
