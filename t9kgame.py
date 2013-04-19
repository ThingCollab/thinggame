import pygame, sys, os, urllib, cStringIO
from pygame.locals import *

pygame.init()

pygame.display.set_caption('t9k Unofficial Collaborative Game')
screen = pygame.display.set_mode((640, 480))
screen = pygame.display.get_surface()
file = cStringIO.StringIO(urllib.urlopen("http://images.wikia.com/smileyofawesome/images/b/bc/Wiki.png").read())
smiley = pygame.image.load(file)
screen.blit(smiley, (320-smiley.get_size()[0]*0.5,240-smiley.get_size()[1]*0.5))
pygame.display.flip()

size = screen.get_size()

vel = [0,0]
pos = [320-smiley.get_size()[0]*0.5,240-smiley.get_size()[1]*0.5]
damping = 0.99

pygame.key.set_repeat(10,10)

def moveSmiley(acc):
	global vel, pos, damping
	for i in range(len(pos)):
		vel[i]+=acc[i]
		pos[i]+=vel[i]
		if pos[i] > screen.get_size()[i]-smiley.get_size()[i] or pos[i] < 0:
			vel[i]*=-1
			pos[i] = max(0,min(screen.get_size()[i]-smiley.get_size()[i],pos[i]))
		vel[i]*=damping
	screen.fill((63,127,255));
	screen.blit(smiley, pos)
	pygame.display.flip()


def input(events):
	acc = [0,0]
	global vel, pos, damping
	if pygame.key.get_pressed()[K_UP]:
		acc[1] -=1
	if pygame.key.get_pressed()[K_DOWN]:
		acc[1] +=1
	if pygame.key.get_pressed()[K_RIGHT]:
		acc[0] +=1
	if pygame.key.get_pressed()[K_LEFT]:
		acc[0] -=1
	
#	print str(acc[0]) + ' ' + str(acc[1])
	moveSmiley(acc)
	for event in events:
		if event.type == QUIT:
			sys.exit(0)
while True:
	input(pygame.event.get())

