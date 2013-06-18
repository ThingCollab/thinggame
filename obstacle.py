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
