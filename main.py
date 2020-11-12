﻿#!/usr/bin/python3
# -*- coding: Utf-8 -*


import pygame
from pygame.locals import *

# importation of moduls

from labyrinth import Labyrinth
import constants as constants
from macgyver import Macgyver

# Window initialization

pygame.init()
screen = pygame.display.set_mode((constants.WINDOW_SIZE , constants.WINDOW_SIZE))
pygame.display.set_caption(constants.WINDOW_TITLE)
image_font = pygame.image.load(constants.IMAGE_FONT)


# Main loop 

run = True

while run:
	
	pygame.time.Clock().tick(30)
	screen.blit(image_font, (0, 0))
	
	
	"""instances of classes"""
	lab = Labyrinth(screen)
	mac = Macgyver(lab)
	lab.display_hero(0, 14)	

	
	for e in pygame.event.get():
		if e.type == pygame.QUIT or e.type == KEYDOWN and e.key == K_SPACE :
        	 run = False
		elif e.type == KEYDOWN and e.key == K_RIGHT :
			mac.move_right()
	lab.display_hero(mac.x, mac.y)

		
	pygame.display.flip()
	
	

       
			
				
       
