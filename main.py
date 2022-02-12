from imports import *

pygame.init()

display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

    
player = Player(400,300,32,32)

level = 1
timeSinceLevelStart = 0
timeToNextLevel = 300

display_scroll = [0,0]

all_sprites.add(player)

# Game loop
while True:
    dt = clock.tick()
    GLOBAL_TIME += dt
    timeSinceLevelStart += dt
    display.fill((24,164,86))
    
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet = PlayerBullet(player.x,player.y,mouse_x,mouse_y,GLOBAL_TIME)
                addBullet(bullet)
    keys = pygame.key.get_pressed()
    
    controller(keys,display_scroll,SPEED,non_player_sprites)
    # pygame.draw.rect(display,(255,255,255),(100-display_scroll[0],100-display_scroll[1],16,16))
    generateEnemies(level)    
    for sprite in all_sprites:
        sprite.main(display)
        sprite.update(GLOBAL_TIME,player)
    for enemy in enemies:
        enemy.moveToPlayer(player)
    clock.tick(60)
    
    if timeSinceLevelStart >= timeToNextLevel:
        level += 1
        timeSinceLevelStart = 0
        timeToNextLevel += (100 + 10*level)
    
    f = pygame.font.SysFont("Verdana",20)
    g = f.render(str(level),True,(255,255,255))
    display.blit(g,(400,10))
    
    p = f.render(str(player.points),True,(255,255,255))
    display.blit(p,(600,10))
    
    pygame.display.update()
    
    