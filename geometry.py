import math
from math import *

def length(vector):
	return sqrt(vector[0] ** 2 + vector[1] ** 2)

def normalize(vector):
	d = length(vector)
	if d > 0:
		return [vector[0]/d,vector[1]/d]
	else:
		return [1,0]

def distance(vector1, vector2):
	return sqrt((vector1[0]-vector2[0])**2 + (vector1[1]-vector2[1])**2)

def vecAdd(vector1, vector2):
	return [vector1[0]+vector2[0],vector1[1]+vector2[1]]

def vecSub(vector1, vector2):
	return [vector1[0]-vector2[0],vector1[1]-vector2[1]]

def vecMul(vector1, vector2):
	return [vector1[0]*vector2[0],vector1[1]*vector2[1]]
