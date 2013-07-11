import pygame, urllib, cStringIO, xml.etree.ElementTree as ET, zlib, base64, array
from pygame import *
from tile import *
from entity import *
from projectile import *
from spritesheet import *


class level:
	def __init__(self):
		self.state = "Level"
		self.allGroup = pygame.sprite.Group()
		self.entityGroup = pygame.sprite.Group()
		self.tileGroup = pygame.sprite.Group()
		self.obstacleGroup = pygame.sprite.Group()
		self.waterGroup = pygame.sprite.Group()
		self.lavaGroup = pygame.sprite.Group()
		self.projectileGroup = pygame.sprite.Group()
		self.tileSet = spritesheet("Basic Tileset.png",32)
		Tile.groups = self.allGroup, self.tileGroup
		entity.groups = self.allGroup, self.entityGroup
		projectile.groups = self.allGroup, self.projectileGroup
		self.levelSurface = pygame.display.set_mode((736, 480))
	def load(self):
		tiles = []
		tree = ET.parse('Basic Level.tmx')
		root = tree.getroot()
		tileProperties = []
		for layer in root.iter('tile'):
			tileProperty = {'tileNum' : layer.attrib['id']}
#			print layer.tag, layer.attrib
			for g in layer:
				tileProperty[g[0].attrib['name']] = g[0].attrib['value']
			tileProperties.append(tileProperty)
#		print tileProperties
		for layer in root.iter('layer'):
#			print layer.tag, layer.attrib['name']
#			print "\t" + layer[0].tag, layer[0].attrib
			data = layer[0].text.encode('ascii')
			encoding = layer[0].attrib.pop('encoding')
			if encoding == 'base64':
				data = base64.b64decode(data)
			data = zlib.decompress(data)
			tlayer = array.array('L', [(ord(a) +(ord(b) << 8) + (ord(c) << 16) + (ord(d) << 24)) for a, b, c, d in zip(*(data[x::4] for x in range(4)))])
			for y in range(0,15):
				for x in range(0,23):
					if layer.attrib['name'] == "Background Tiles" and not tlayer[y*23+x] == 1:
						tileNum = tlayer[y*23+x]
						tileType = 0
						for tileProperty in tileProperties:
							if tileProperty['tileNum'] == str(tileNum): tileType = int(tileProperty['type'])
#						print tileNum, tileType
						tiles.append(Tile((32*x, 32*y), tileType, tileNum, self.tileSet))
		entities = []
		levelArray = [
					  "OOOOOOOOOOOOOOOOOOOOOOO",
					  "O                     O",
					  "O                     O",
					  "O  0                  O",
					  "O  OOOOO  WWW  L   L  O",
					  "O    O   W   W L  L   O",
					  "O    O   W   W L L    O",
					  "O    O    WWW  LL     O",
					  "O    O       W L L    O",
					  "O    O       W L  L   O",
					  "O    O    WWW  L   L  O",
					  "O                     O",
					  "O                     O",
					  "O  2  2   2  2      2 O",
					  "OOOOOOOOOOOOOOOOOOOOOOO",]
		x = y = 0
		for row in levelArray:
			for column in row:
				if column == "0": entities.append(entity((x,y),0))
				elif column == "2": entities.append(entity((x,y),2))
				x += 32
			y += 32
			x = 0
	def unload(self):
		for item in self.allGroup: item.kill()
	def update(self):
		self.levelSurface.fill((63,127,255));
		self.entityGroup.update(self.tileGroup, self.entityGroup, self.projectileGroup)
		self.projectileGroup.update(self.tileGroup)
		self.tileGroup.update()
		self.projectileGroup.draw(self.levelSurface)
		self.entityGroup.draw(self.levelSurface)
		self.tileGroup.draw(self.levelSurface)
		pygame.display.flip()
	def writeLevel(self):
		print "TILES"
		for tile in self.tileGroup:
			print str(tile.type)+"\t"+str(tile.pos)+"\t"
		for entity in self.entityGroup:
			print str(entity.type)+"\t"+str(entity.pos)+"\t"+str(entity.vel)+"\t"+str(entity.health)
		for projectile in self.projectileGroup:
			print str(projectile.type)+"\t"+str(projectile.pos)+"\t"+str(projectile.vel)+"\t"+str(projectile.targetTypes)
