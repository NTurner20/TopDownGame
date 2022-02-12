import pygame
def eventHandler(keys,display_scroll,SPEED,player_bullets):
    # Event Handler
    if keys[pygame.K_a]:
        display_scroll[0] -= SPEED
        for bullet in player_bullets:
            bullet.x += SPEED
    if keys[pygame.K_d]:
        display_scroll[0] += SPEED
        for bullet in player_bullets:
            bullet.x -= SPEED    
    if keys[pygame.K_w]:
        display_scroll[1] -= SPEED
        for bullet in player_bullets:
            bullet.y += SPEED
    if keys[pygame.K_s]:
        display_scroll[1] += SPEED
        for bullet in player_bullets:
            bullet.y -= SPEED
    