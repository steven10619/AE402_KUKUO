# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:21:59 2021

@author: carols1107
"""
import pygame
import random

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

all_list = pygame.sprite.Group()

for i in range(50):
    block = Block(Black, 20, 15)
    block.rect.x = random.randrange(screen_width) 
    block.rect.y = random.randrange(screen_height)
    all_list.add(block)
    
player = Block(Red, 20, 15)    
player.rect.x = 0
player.rect.y = 0   
all_list.add(player)

done = False

clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(White)
    
    all_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()




    