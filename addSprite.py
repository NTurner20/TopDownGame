import pygame
from groups import *

def addToAll(sprite):
    player_bullets.add(sprite)
    all_sprites.add(sprite)
    enemies.add(sprite)
    non_player_sprites.add(sprite)

def addBullet(sprite):
    player_bullets.add(sprite)
    all_sprites.add(sprite)
    non_player_sprites.add(sprite)

def addEnemy(sprite):
    enemies.add(sprite)
    all_sprites.add(sprite)
    non_player_sprites.add(sprite)