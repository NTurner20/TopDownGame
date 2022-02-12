import pygame
import math
class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,mouse_x,mouse_y,GLOBAL_TIME):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y =y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y - mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle)*self.speed
        self.y_vel = math.sin(self.angle)*self.speed
        self.start_time = GLOBAL_TIME
        self.kill_time = 15
    def main(self,display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        pygame.draw.circle(display, (0,0,0),(self.x,self.y),5)
    def update(self,GLOBAL_TIME):
        if GLOBAL_TIME > self.start_time + self.kill_time:
            self.kill()       
    