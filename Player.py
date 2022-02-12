import pygame
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        pygame.draw.rect(display,(255,0,0),(self.x,self.y,self.width,self.height))