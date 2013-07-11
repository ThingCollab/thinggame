import pygame, urllib, cStringIO
from pygame import *
from spritesheet import *

file = cStringIO.StringIO(urllib.urlopen("Basic Tileset.png").read())
tileset = pygame.image.load(file)

class Tile(pygame.sprite.Sprite):
	width = 32
	height = 32
	type = 0
#	Types:
#	0: Air
#	1: Obstacle
#	2: Water
#	3: Lava
	def __init__(self, startpos, starttype, tilenum, ss):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.ss = ss
		self.pos = startpos
		self.type = starttype
		self.image = self.ss.image_at(tilenum-1)
		self.rect = self.image.get_rect()
		if self.type == 3: self.image.set_alpha(127)
		if self.type == 4: self.image.set_alpha(239)
	def update(self):
		self.rect.topleft = self.pos
