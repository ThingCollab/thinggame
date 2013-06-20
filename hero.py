import pygame, urllib, cStringIO, math
from pygame import *
from projectile import *
from math import *

file = cStringIO.StringIO(urllib.urlopen("http://images.wikia.com/smileyofawesome/images/b/bc/Wiki.png").read())
smiley = pygame.transform.smoothscale(pygame.image.load(file), (32,32))

class hero(pygame.sprite.Sprite):
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.health = 100
		self.vel = [0,0]
		self.image = smiley
		self.rect = self.image.get_rect()
		self.rect.topleft = startpos
		self.ground = False
		self.shooting = False
	def update(self, obstacles, enemies, projectiles):
		acc = [0,0]
		jump = 0
		if pygame.key.get_pressed()[K_SPACE]:
			if self.ground: self.vel[1] -= 15
		self.vel[0] = 0
		if pygame.key.get_pressed()[K_RIGHT]:
			self.vel[0] =  5
		if pygame.key.get_pressed()[K_LEFT]:
			self.vel[0] = -5
		if pygame.mouse.get_pressed()[0] and not self.shooting:
			self.shooting = True
			vel = [mouse.get_pos()[0]-self.rect.centerx,mouse.get_pos()[1]-self.rect.centery]
			d = sqrt(vel[0] ** 2 + vel[1] ** 2)
			if not d == 0:
				vel[0]*= 5/d
				vel[1]*= 5/d
			else:
				vel = [5,0]
			myProjectile = projectile(self.rect.center, vel)
			projectiles.add(myProjectile)
		elif not pygame.mouse.get_pressed()[0]:
			self.shooting = False
		if not self.ground:
			self.vel[1] += 1;
		self.rect.left += self.vel[0]
		self.obstacleCollide(self.vel[0], 0, obstacles)
		self.rect.top += self.vel[1]
		self.ground = False
		self.obstacleCollide(0, self.vel[1], obstacles)
		for enemy in enemies:
			if sprite.collide_rect(self, enemy):
				self.health -= enemy.touchDamage
				print "Enemy has dealt " + str(enemy.touchDamage) + " damage to the player. New health is " + str(self.health) + "."
		if self.health <= 0:
			self.kill()

	def obstacleCollide(self, velX, velY, obstacles):
		for obstacle in obstacles:
			if sprite.collide_rect(self, obstacle):
				if velX > 0: self.rect.right = obstacle.rect.left
				if velX < 0: self.rect.left = obstacle.rect.right
				if velY > 0:
					self.rect.bottom = obstacle.rect.top
					self.ground = True
					self.vel[1] = 0
				if velY < 0: self.rect.top = obstacle.rect.bottom

