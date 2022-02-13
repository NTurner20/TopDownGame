from decimal import Clamped
from imports import pygame, math, random
from groups import player_bullets, enemies
from addSprite import *


def clamp(num, min_value, max_value):
        num = max(min(num, max_value), min_value)
        return num
    

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,player,level):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.distToPlayer = math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
        self.radius = random.randrange(17,55)
        self.speed = 30/self.radius + level
        self.r_value = 128
        self.g_value = clamp(30 + 30*self.speed**1.7,0,255)
        self.b_value = 100
        self.r_value2 = 0
        if self.radius > 30:
            self.hits = 2
            self.r_value2 = clamp(148 + self.radius/2,0,255)
        else:
            self.hits = 1
    def main(self,display):
        pygame.draw.circle(display,color = (self.r_value,self.g_value,self.b_value),center = (self.x,self.y),radius = self.radius)
        if self.radius > 30:
            pygame.draw.circle(display,color = (self.r_value2,self.g_value,self.b_value),center = (self.x,self.y),radius = self.radius/2)
    def update(self,GLOBAL_TIME,player):
        for bullet in player_bullets:
            minDist = self.radius/2 + bullet.radius/2
            if math.sqrt((self.x - bullet.x)**2 + (self.y - bullet.y)**2) <= minDist:
                self.hits -= 1
                if self.hits == 0:
                    bullet.kill()
                    self.kill()
                    player.points += 1
                else:
                    bullet.kill()
                    player.points += 1
                    self.radius /= 2
                    self.speed = 30/self.radius
                    self.r_value = self.r_value2
        if math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2) <= self.radius:
            player.gameOver = True
            
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
            
def generateEnemies(level,player):
    if len(enemies) < level + 3:
        e = Enemy(random.randrange(0,400),random.randrange(0,600),player,level)
        while e.distToPlayer < 70:
            e = Enemy(random.randrange(0,400),random.randrange(0,600),player,level)
        addEnemy(e)