import pygame, urllib, cStringIO, math
from pygame import *
from projectile import *
from geometry import *

file = cStringIO.StringIO(urllib.urlopen("http://images.wikia.com/smileyofawesome/images/b/bc/Wiki.png").read())
smiley = pygame.transform.smoothscale(pygame.image.load(file), (32,32))

class hero(pygame.sprite.Sprite):
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.health = 1000000
		self.vel = [0,0]
		self.image = smiley
		self.rect = self.image.get_rect()
		self.pos = [startpos[0],startpos[1]]
		self.rect.topleft = startpos
		self.ground = False
		self.water = False
		self.lava = False
		self.shooting = False
	def update(self, obstacleTiles, waterTiles, lavaTiles, enemies, projectiles):
		acc = [0,0]
		jump = 0
# Apply keyboard velocity
		if pygame.key.get_pressed()[K_RIGHT]: self.vel[0] =  5
		if pygame.key.get_pressed()[K_LEFT]: self.vel[0] = -5
# Create Projectiles
		if (pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[K_z]) and not self.shooting:
			self.shooting = True
			vel = [mouse.get_pos()[0]-self.rect.centerx,mouse.get_pos()[1]-self.rect.centery]
			vel = vecMul(normalize(vel),[10,10])
			myProjectile = projectile(self.rect.center, vel, enemies)
			projectiles.add(myProjectile)
		elif not pygame.mouse.get_pressed()[0]: self.shooting = False
# Do water collision
		self.water = False
		for wTile in waterTiles:
			if sprite.collide_rect(self, wTile): self.water = True
		if self.water: self.vel = vecMul(self.vel, [0.25,0.25])
# Do lava collision
		self.lava = False
		for lTile in lavaTiles:
			if sprite.collide_rect(self, lTile): self.lava = True
		if self.lava:
			self.health -= 10
			self.vel = vecMul(self.vel, [0.1,0.1])
# Apply jumping velocity
		if pygame.key.get_pressed()[K_SPACE]:
			if self.ground: self.vel[1] -= 15
			if self.water: self.vel[1] -= 5
			if self.lava: self.vel[1] -= 1.5
# Apply gravity, integrate position and do obstacle collision
		if not self.ground: self.vel[1] += 1;
		self.pos[0] += self.vel[0]
		self.rect.left = self.pos[0]
		self.obstacleCollide(self.vel[0], 0, obstacleTiles)
		self.pos[1] += self.vel[1]
		self.rect.top = self.pos[1]
		self.ground = False
		self.obstacleCollide(0, self.vel[1], obstacleTiles)
# Do enemy collision
		for enemy in enemies:
			if sprite.collide_rect(self, enemy):
				self.health -= enemy.touchDamage
		if self.health <= 0:
			self.kill()
# Reset horizontal velocity
		self.vel[0] = 0


	def obstacleCollide(self, velX, velY, obstacleTiles):
		for oTile in obstacleTiles:
			if sprite.collide_rect(self, oTile):
				if velX > 0:
					self.rect.right = oTile.rect.left
					self.pos[0] = self.rect.left
				if velX < 0:
					self.rect.left = oTile.rect.right
					self.pos[0] = self.rect.left
				if velY > 0:
					self.rect.bottom = oTile.rect.top
					self.ground = True
					self.vel[1] = 0
					self.pos[1] = self.rect.top
				if velY < 0:
					self.rect.top = oTile.rect.bottom
					self.pos[1] = self.rect.top

