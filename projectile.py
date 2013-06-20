import pygame, urllib, cStringIO
from pygame import *

class projectile(pygame.sprite.Sprite):
	width = 8
	height = 8
	damage = 50
	vel = [0,0]
	def __init__(self, startpos, startvel):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.pos = startpos
		self.vel = startvel
		self.image = pygame.Surface((self.width,self.height))
		self.image.fill((255,0,0,0))
		self.rect = self.image.get_rect()
		self.rect.center = startpos

	def update(self, obstacles, enemies):
		self.rect.centerx += self.vel[0]
		self.rect.centery += self.vel[1]
		for enemy in enemies:
			if sprite.collide_rect(self, enemy):
				enemy.health -= self.damage
				self.kill()
		for obstacle in obstacles:
			if sprite.collide_rect(self, obstacle):
				self.kill()

