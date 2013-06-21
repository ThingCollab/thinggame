import pygame, sys, os, urllib, cStringIO
from pygame.locals import *
from level import *
pygame.init()

pygame.display.set_caption('t9k Unofficial Collaborative Game')

mainScreen = pygame.display.set_mode((736, 480))
mainScreen = pygame.display.get_surface()
background = pygame.Surface((mainScreen.get_width(),mainScreen.get_height()))

myLevel = level((10,10))

pygame.display.flip()

size = mainScreen.get_size()
paused = 0

def input(events):
	global paused
	if paused == 0:
		myLevel.update()
	else:
		font = pygame.font.Font(None, 36)
		text = font.render("Paused", 1, (255, 10, 10))
		textpos = text.get_rect()
		textpos.centerx = mainScreen.get_rect().centerx
		textpos.centery = mainScreen.get_rect().centery
		mainScreen.blit(text, textpos)
		pygame.display.flip()
	
	for event in events:
		if event.type == KEYDOWN:
			if event.key == K_p:
				paused = 1 - paused
		if event.type == QUIT:
			sys.exit(0)
while True:
	input(pygame.event.get())

