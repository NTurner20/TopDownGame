import sys
import math
from eventHandler import pygame
from eventHandler import eventHandler
from Player import Player

SPEED = 5
GLOBAL_TIME = 0


pygame.init()

display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

class PlayerBullet:
    def __init__(self,x,y,mouse_x,mouse_y):
        self.shoot_start = GLOBAL_TIME
        self.x = x
        self.y =y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y - mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle)*self.speed
        self.y_vel = math.sin(self.angle)*self.speed
    def main(self,display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        pygame.draw.circle(display, (0,0,0),(self.x,self.y),5)
           
        
    
    
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
    
    