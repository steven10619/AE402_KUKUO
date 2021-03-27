# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:31:04 2021

@author: carols1107
"""
import pygame,random

Black = (0, 0, 0)
Red = (225, 0 , 0)
White = (254, 254, 254)

   

pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("方塊")


clock = pygame.time.Clock()

done = False
x = 0
y = 0 

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(Black)
    pygame.draw.rect(screen, Red, [x, y, 25, 25])
    pygame.draw.rect(screen, Black, [x, y, 10, 10])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        x = random.randrange(0,700)
        y = random.randrange(0,400) 
    if keys[pygame.K_LEFT]:
        x = x-20
    if keys[pygame.K_UP]:
        y = y-20
    if keys[pygame.K_RIGHT]:
        x = x+20
    if keys[pygame.K_DOWN]:
        y = y+20
    
    pygame.display.flip()
    
    pygame.init()
    done = False
                

                
    
    
   
   
clock.tick(60)
pygame.quit() 