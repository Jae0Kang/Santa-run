#from operator import truediv
import sys
import pygame
import os
import random
from AnimatedSprite import*

pygame.init()
width_screen = 1200
height_screen = 600


display_surface = pygame.display.set_mode((width_screen, height_screen))    
time_clok = pygame.time.Clock()                                             
pygame.display.set_caption("Santa run")                                      

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (0xec, 0xec, 0xec)
clock = pygame.time.Clock()
FPS = 30
BACKGROUND_COLOR = pygame.Color('white')

player = AnimatedSprite(position=(100, 440))
all_sprites = pygame.sprite.Group(player) 
grounds = pygame.sprite.Group()
grounds.add(Ground(0, 550, 600, 200, GREY))
grounds.add(Ground(600, 550, 600, 200, GREY))
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.isJump = True  
    player.jump()
    all_sprites.update()   
    display_surface.fill(BACKGROUND_COLOR)
    all_sprites.draw(display_surface)
    grounds.draw(display_surface)
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()


