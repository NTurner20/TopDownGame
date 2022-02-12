import pygame
def eventHandler(keys,display_scroll,SPEED,non_player_sprites):
    # Event Handler
    if keys[pygame.K_a]:
        display_scroll[0] -= SPEED
        for sprite in non_player_sprites:
            sprite.x += SPEED
    if keys[pygame.K_d]:
        display_scroll[0] += SPEED
        for sprite in non_player_sprites:
            sprite.x -= SPEED    
    if keys[pygame.K_w]:
        display_scroll[1] -= SPEED
        for sprite in non_player_sprites:
            sprite.y += SPEED
    if keys[pygame.K_s]:
        display_scroll[1] += SPEED
        for sprite in non_player_sprites:
            sprite.y -= SPEED
    