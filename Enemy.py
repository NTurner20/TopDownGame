from decimal import Clamped
from imports import pygame, math, random
from groups import player_bullets, enemies, shotgun_bullets
from addSprite import *
from Ammo import *
from string import Template
import time
def clamp(num, min_value, max_value):
        num = max(min(num, max_value), min_value)
        return num
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,player,level):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.level = level
        self.distToPlayer = math.sqrt((self.x - (player.x+16))**2 + (self.y - (player.y+16))**2)
        # init location, no. of hits
        self.setNumOfHits()
        # no. of hits determines radius
        self.setRadius()
        # radius inverse with speed
        self.setSpeed()
        # Speed determines color
        self.r_values = []
        self.setRGB()
    def main(self,display):
        # Draw Circle(s)
        self.draw(display)
    def spawnAmmo(self,x,y,player):
        if random.randint(0,6) == 1:
            a = Ammo(x,y,player)
            addAmmo(a)
    def update(self,GLOBAL_TIME,player):
        # Detect Bullet Collision
        for bullet in player_bullets:
            minDist = self.radius + bullet.radius
            if math.sqrt((self.x - bullet.x)**2 + (self.y - bullet.y)**2) <= minDist:
                self.hits -= 1
                player.points += 1
                if not shotgun_bullets.has(bullet):
                    bullet.kill()
                if self.hits > 0:
                    if self.hits == 2:
                        self.radius *= 2/3
                        self.setSpeed()
                        self.r_value1 = self.r_value2
                        self.r_value2 = self.r_value3
                    if self.hits == 1:
                        self.radius /= 2
                        self.setSpeed()
                        self.r_value1 = self.r_value2
                else:
                    self.kill()
                    self.spawnAmmo(self.x,self.y,player)
        # Detect Player Collision
        if math.sqrt((self.x - (player.x+16))**2 + (self.y - (player.y+16))**2) <= self.radius + 16:
            player.gameOver = True
            
    def moveToPlayer(self,player):
        distToPlayer = math.sqrt((self.x - player.x-16)**2 + (self.y - player.y-16)**2)
        angleToPlayer = math.atan2(abs(self.y-(player.y+16)),abs(self.x-(player.x+16)))
        if distToPlayer > 20: 
            if self.x < player.x:
                self.x += math.cos(angleToPlayer)*self.speed
            else:
                self.x -= math.cos(angleToPlayer)*self.speed
            if self.y < player.y:
                self.y += math.sin(angleToPlayer)*self.speed
            else:
                self.y -= math.sin(angleToPlayer)*self.speed
        if distToPlayer > 1000:
            self.kill()
    def setNumOfHits(self):
        if self.level > 7:
            self.hits = 3
        elif self.level > 3:
            self.hits = 2
        else:
            self.hits = 1
    
    def setRadius(self):
        if self.hits == 1:
            self.radius = random.randint(15,30)
        if self.hits == 2:
            self.radius = random.randint(30,60)
        if self.hits == 3:
            self.radius = random.randint(60,90)
    def setSpeed(self):
        self.speed = 30/self.radius + self.level/5
    def setRGB(self):
        if self.hits == 1:
            self.r_value2 = 0
            self.r_value3 = 0
        if self.hits == 2:
            self.r_value2 = clamp(98 + self.radius/2,0,255)
            self.r_value3 = 0
        if self.hits == 3:
            self.r_value2 = clamp(98 + self.radius/2,0,255)
            self.r_value3 = clamp(58 + self.radius/3,0,255)  
        self.r_value1 = 168
        self.g_value = clamp(30 + 20*self.speed**1.7,0,255)
        self.b_value = clamp(70 + self.speed**1.1,0,255)
        self.r_values=[self.r_value1,self.r_value2,self.r_value3]
    def draw(self,display):
        if self.hits == 1:
            pygame.draw.circle(display,color = (self.r_values[0],self.g_value,self.b_value),center = (self.x,self.y),radius = self.radius)
        if self.hits == 2:
            pygame.draw.circle(display,color = (self.r_values[1],self.g_value,self.b_value),center = (self.x,self.y),radius = self.radius)
            pygame.draw.circle(display,color = (self.r_values[0],self.g_value,self.b_value),center = (self.x,self.y),radius = self.radius/2)
        if self.hits == 3:
            pygame.draw.circle(display,color = (self.r_values[2],self.g_value,self.b_value),center = (self.x,self.y),radius = self.radius)
            pygame.draw.circle(display,color = (self.r_values[1],self.g_value,self.b_value),center = (self.x,self.y),radius = self.radius*2/3)
            pygame.draw.circle(display,color = (self.r_values[0],self.g_value,self.b_value),center = (self.x,self.y),radius = self.radius/3)
def generateEnemies(level,player):
    if len(enemies) < level + 1:
        e = Enemy(random.randrange(0,500),random.randrange(0,700),player,level)
        while e.distToPlayer < 220:
            e = Enemy(random.randrange(0,400),random.randrange(0,600),player,level)
        # time.sleep(2)
        addEnemy(e)
    