from imports import pygame
from imports import math

class Ammo(pygame.sprite.Sprite):
    def __init__(self,x,y,player):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
    def main(self,display):
        pygame.draw.rect(display,(200,20,50),(self.x,self.y,20,20))
    def update(self,GLOBAL_TIME,player): 
        if math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2) < 26:
            player.ammo += 5
            self.kill()    