from math import radians
from PlayerBullet import PlayerBullet
from addSprite import addBullet, addShotgun
from imports import math

def shotgun(player,mouse_x,mouse_y,GLOBAL_TIME):
    if player.ammo > 0:
        player.ammo -= 1
        for i in range(-1,1):
            p = PlayerBullet(player.x,player.y,mouse_x,mouse_y,GLOBAL_TIME)
            p.angle += i*radians(20)
            p.speed += 3
            p.r_value = 255
            p.x_vel = math.cos(p.angle)*p.speed
            p.y_vel = math.sin(p.angle)*p.speed    
            addShotgun(p)
        
    