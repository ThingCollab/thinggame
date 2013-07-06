import pygame, urllib, cStringIO, math
from pygame import *
from projectile import *
from geometry import *

file = cStringIO.StringIO(urllib.urlopen("Smiley.png").read())
smiley = pygame.transform.smoothscale(pygame.image.load(file), (32,32))

class entity(pygame.sprite.Sprite):
	def __init__(self, startpos, type):
		pygame.sprite.Sprite.__init__(self, self.groups)
		line = []
		self.type = type
		with open("Entities.dat") as file: line = file.read().splitlines()[type].split()
		self.name = line[1]
		self.enemies = map(int, line[2].split(','))
		self.health = int(line[3])
		self.userControl = line[4] == 'True'
		self.touchDamage = 5
		self.vel = [2,0]
		self.image = smiley
		self.rect = self.image.get_rect()
		self.pos = [startpos[0],startpos[1]]
		self.rect.topleft = startpos
		self.ground = False
		self.water = False
		self.lava = False
		self.shooting = False
	def update(self, tiles, entities, projectiles):
		if self.userControl:
		# Apply keyboard velocity
			if pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]: self.vel[0] =  5
			if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]: self.vel[0] = -5
		# Create Projectiles
			if (pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[K_z]) and not self.shooting:
				self.shooting = True
				vel = [mouse.get_pos()[0]-self.rect.centerx,mouse.get_pos()[1]-self.rect.centery]
				vel = vecMul(normalize(vel),[10,10])
				myProjectile = projectile(self, vel, entities, self.enemies)
				projectiles.add(myProjectile)
			elif not pygame.mouse.get_pressed()[0]: self.shooting = False
			
		# Do tile collision
		self.water = False
		self.lava = False
		for tile in tiles:
			if sprite.collide_rect(self, tile):
				if tile.type == 2: self.water = True
				if tile.type == 3: self.lava = True
		if self.water: self.vel = vecMul(self.vel, [0.25,0.25])
		if self.lava:
			self.health -= 10
			self.vel = vecMul(self.vel, [0.1,0.1])
		# Apply jumping velocity
		if self.userControl and pygame.key.get_pressed()[K_SPACE]:
			if self.ground: self.vel[1] -= 15
			if self.water: self.vel[1] -= 5
			if self.lava: self.vel[1] -= 1.5
		# Apply gravity, integrate position and do obstacle collision
		if not self.ground: self.vel[1] += 1;
		self.pos[0] += self.vel[0]
		self.rect.left = self.pos[0]
		self.obstacleCollide(self.vel[0], 0, tiles)
		self.pos[1] += self.vel[1]
		self.rect.top = self.pos[1]
		self.ground = False
		self.obstacleCollide(0, self.vel[1], tiles)
		# Do enemy collision
		for entity in entities:
			if self.userControl and any(entity.type == enemyType for enemyType in self.enemies) and sprite.collide_rect(self, entity):
				self.health -= entity.touchDamage
		if self.health <= 0:
			self.kill()
		# Reset horizontal velocity
		if self.userControl: self.vel[0] = 0
		else:
			if self.vel[0] < 0: self.vel[0] = -2
			else: self.vel[0] = 2	
	
	def obstacleCollide(self, velX, velY, obstacleTiles):
		for oTile in obstacleTiles:
			if sprite.collide_rect(self, oTile) and oTile.type == 1:
				if velX > 0:
					self.rect.right = oTile.rect.left
					self.pos[0] = self.rect.left
					if not self.userControl: self.vel[0] *= -1
				if velX < 0:
					self.rect.left = oTile.rect.right
					self.pos[0] = self.rect.left
					if not self.userControl: self.vel[0] *= -1
				if velY > 0:
					self.rect.bottom = oTile.rect.top
					self.ground = True
					self.vel[1] = 0
					self.pos[1] = self.rect.top
				if velY < 0:
					self.rect.top = oTile.rect.bottom
					self.pos[1] = self.rect.top

