import sys
import math
from eventHandler import pygame
from eventHandler import eventHandler
from Player import Player
from PlayerBullet import PlayerBullet

SPEED = 5
GLOBAL_TIME = 0


pygame.init()

display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
    
player = Player(400,300,32,32)

display_scroll = [0,0]
player_bullets = []

while True:
    dt = clock.tick()
    GLOBAL_TIME += dt
    display.fill((24,164,86))
    
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x,player.y,mouse_x,mouse_y))
    
    keys = pygame.key.get_pressed()
    eventHandler(keys,display_scroll,SPEED,player_bullets)
    pygame.draw.rect(display,(255,255,255),(100-display_scroll[0],100-display_scroll[1],16,16))
    
    
    
        
    player.main(display)
    
    for bullet in player_bullets:
        bullet.main(display)
    
    
    
    clock.tick(60)
    pygame.display.update()
    
    