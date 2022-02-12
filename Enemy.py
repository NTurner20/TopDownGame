import pygame
from groups import player_bullets
import math
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.radius = 30
    def main(self,display):
        pygame.draw.circle(display,(128,56,67),center = (self.x,self.y),radius = self.radius)
    def update(self,GLOBAL_TIME):
        for bullet in player_bullets:
            minDist = self.radius/2 + bullet.radius/2
            if math.sqrt((self.x - bullet.x)**2 + (self.y - bullet.y)**2) <= minDist:
                bullet.kill()
                self.kill()