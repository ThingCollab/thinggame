# Modified from source at http://www.pygame.org/wiki/Spritesheet

import pygame

class spritesheet(object):
	def __init__(self, filename, tileSize):
		self.tileSize = tileSize
		self.sheet = pygame.image.load(filename)
	def image_at(self, tileNum):
		rect = pygame.Rect(self.tileSize*tileNum%int(self.sheet.get_width()),self.tileSize*int(tileNum/self.sheet.get_height()),self.tileSize,self.tileSize)
		image = pygame.Surface(rect.size)
		image.blit(self.sheet, (0, 0), rect)
		return image
	def images_at(self, tileNums):
		return [self.image_at(tileNum) for tileNum in tileNums]
