import pygame, sys, os, urllib, cStringIO
from pygame.locals import *
from level import *
pygame.init()

pygame.display.set_caption('t9k Unofficial Collaborative Game')

mainScreen = pygame.display.set_mode((736, 480))
mainScreen = pygame.display.get_surface()
background = pygame.Surface((mainScreen.get_width(),mainScreen.get_height()))

keyBindings = {'paused': "k_P"}

states = []
states.append(level())
# states.append(<all of the menus>)
# I really don't understand how Python's memory management system works, so this will probably be
# an inefficient way to use memory.

pygame.display.flip()

size = mainScreen.get_size()
paused = False

currentState = states[0]

#	Changing states:
# Every level and menu will need to have a "state" variable, and a load() and unload() method
# When you change a state, the current state will unload, then the new state will load
#	Potential problems:
# Loading a level will require input data (which level, save files).
#	Possible solution: overload the changeState function (can python overload functions?)
#	to allow for input data to be passed to the level's load function.
# In-game options would require two states to be loaded simultaneously.
#	Possible solution: don't make the in-game options loadable via the state system. I
#	think I'll make it so that the level can load and unload the options menu manually.


def changeState(newState):
	global currentState
	currentState.unload()
	for state in states:
		if state.state == newState: currentState = state
	currentState.load()

def mainLoop(events):
	global paused
	if currentState.state == "Level":
		if paused:
			font = pygame.font.Font(None, 36)
			text = font.render("Paused", 1, (255, 10, 10))
			textpos = text.get_rect()
			textpos.centerx = mainScreen.get_rect().centerx
			textpos.centery = mainScreen.get_rect().centery
			mainScreen.blit(text, textpos)
			pygame.display.flip()
		else:
			currentState.update()
	
	for event in events:
		if event.type == KEYDOWN:
			if event.key == keyBindings['paused']: paused = not paused
			if event.key == K_w and currentState.state == "Level" : currentState.writeLevel()
			if event.key == K_r: changeState("Level")
			if event.key == K_t: changeState("MainMenu")
		if event.type == QUIT:
			sys.exit(0)
while True:
	mainLoop(pygame.event.get())

