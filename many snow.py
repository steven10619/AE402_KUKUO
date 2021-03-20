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
pygame.display.set_caption("My Game")

snow_list = []

for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])
    
    

done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for i in range(len(snow_list)):
         pygame.draw.circle(screen,White,snow_list[i],2)
         snow_list[i][1] = snow_list[i][1]+1
         
         if snow_list[i][1] > 400:
             y=0
             snow_list[i][1] = y
             x = random.randrange(0, 400)
             snow_list[i][0] = x
            
    screen.fill(Black)
   
    
            
    
    
    
   
    pygame.display.flip()
    clock.tick(60)
pygame.quit()    