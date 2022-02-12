import pygame
from groups import player_bullets, enemies
import math
import random
from addSprite import *
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.radius = random.randrange(17,60)
        self.speed = 30/self.radius
        self.r_value = 128
        self.g_value = 40 + 30*self.speed**1.7
        self.b_value = 67
    def main(self,display):
        pygame.draw.circle(display,color = (self.r_value,self.g_value,self.b_value),center = (self.x,self.y),radius = self.radius)
    def update(self,GLOBAL_TIME,player):
        for bullet in player_bullets:
            minDist = self.radius/2 + bullet.radius/2
            if math.sqrt((self.x - bullet.x)**2 + (self.y - bullet.y)**2) <= minDist:
                bullet.kill()
                self.kill()
                player.points += 1
    def moveToPlayer(self,player):
        distToPlayer = math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
        angleToPlayer = math.atan2(abs(self.y-player.y),abs(self.x-player.x))
        if distToPlayer > 20:
            if self.x < player.x:
                self.x += math.cos(angleToPlayer)*self.speed
            else:
                self.x -= math.cos(angleToPlayer)*self.speed
            if self.y < player.y:
                self.y += math.sin(angleToPlayer)*self.speed
            else:
                self.y -= math.sin(angleToPlayer)*self.speed
            
def generateEnemies(level):
    if len(enemies) < level + 3:
        e = Enemy(random.randrange(0,400),random.randrange(0,600))
        addEnemy(e)