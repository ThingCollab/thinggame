import pygame, urllib, cStringIO, math
from pygame import *
from geometry import *


class projectile(pygame.sprite.Sprite):
	width = 8
	height = 8
	damage = 10
	vel = [0,0]
	pos = (0,0)
	homing = True
	homingRange = 25000
	homingWeight = 0.1
	speed = 0
	def __init__(self, startpos, startvel, targetGroup):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.pos = [startpos[0],startpos[1]]
		self.targets = targetGroup
		self.vel = startvel
		self.speed = length(self.vel)
		self.image = pygame.Surface((self.width,self.height))
		self.image.fill((255,0,0,0))
		self.rect = self.image.get_rect()
		self.rect.center = startpos

	def update(self, obstacles):
		if self.homing:
			hasTarget = False
			targetLoc = [0,0]
			for target in self.targets:
				if distance(self.rect.center, target.rect.center) < self.homingRange:
					if not hasTarget:
						targetLoc = target.rect.center
					elif distance(self.rect.center, targetLoc) > distance(self.rect.center, target.rect.center):
						targetLoc = target.rect.center
					hasTarget = True
			if hasTarget:
				modifiedVel = vecAdd(vecMul(self.vel,[1-self.homingWeight,1-self.homingWeight]),vecMul(normalize(vecSub(targetLoc,self.rect.center)),[self.speed*self.homingWeight,self.speed*self.homingWeight]))
				self.vel = vecMul(normalize(modifiedVel), [self.speed,self.speed])
				
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]
		self.rect.center = self.pos
		for target in self.targets:
			if sprite.collide_rect(self, target):
				target.health -= self.damage
				self.kill()
		for obstacle in obstacles:
			if sprite.collide_rect(self, obstacle):
				self.kill()

