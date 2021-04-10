# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:12:01 2021

@author: carols1107
"""

import pygame


Black = (0, 0, 0)
White = (255, 255, 255)

pygame.init()


size = (800,600)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Ship")

clock = pygame.time.Clock()

background_pos = (0,0)
background_img = pygame.image.load("Saturn.jpg").convert()
player_img = pygame.image.load("Ship.png").convert()
player_img.set_colorkey(Black)

click_Sound = pygame.mixer.Sound("laser.ogg")
pygame.mixer.music.load("Background.mp3")
pygame.mixer.music.play()

done = False

while not done :
    screen.fill(Black) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_Sound.play()
    screen.blit(background_img, background_pos)
    player_pos = pygame.mouse.get_pos()
    x =player_pos[0]
    y =player_pos[1]

    screen.blit(player_img,[x-50, y-50])


            
    pygame.display.flip()


clock.tick(60)

pygame.quit()             