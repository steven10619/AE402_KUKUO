# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:31:04 2021

@author: carols1107
"""
import pygame,random

def randColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

   
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

done = False
color = 0
limit = 30
click = False




 

while not done :
    screen.fill(Black) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            click = True
            count = 0
            color = randColor()
            
    if click == True and count < limit:
        pygame.draw.circle(screen, color, pos, count)
        count = count + 1
        if count >= limit:
            click = False
    
    pygame.display.flip()
    done = False
    clock.tick(60)
pygame.quit() 