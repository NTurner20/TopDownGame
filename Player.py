import pygame
from groups import ammo

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,):
        pygame.sprite.Sprite.__init__(self)
        self.points = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gameOver = False
        self.ammo = 20
    def main(self, display):
        pygame.draw.rect(display,(255,0,0),(self.x,self.y,self.width,self.height))
        
    def update(self,GLOBAL_TIME,player):
        pass