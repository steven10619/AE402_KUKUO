# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:31:04 2021

@author: carols1107
"""
import pygame

Black = (0, 0, 0)
White = (225, 225, 225)
Green = (0, 225, 0)

pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(White)
    pygame.draw.polygon(screen, Black,[(700,250), (0,250), (100,50)], 6)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()    

    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
