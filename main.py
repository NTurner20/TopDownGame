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
    gameOver = False
    dt = clock.tick()
    GLOBAL_TIME += dt
    timeSinceLevelStart += dt
    display.fill((24,164,86)) # Background color
    
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet = PlayerBullet(player.x,player.y,mouse_x,mouse_y,GLOBAL_TIME)
                addBullet(bullet)
            if event.button == 3:
                shotgun(player, mouse_x,mouse_y,GLOBAL_TIME)
                
    # Movement ddd
    keys = pygame.key.get_pressed()
    controller(keys,display_scroll,SPEED,non_player_sprites)
    # Enemy generation and movement 
    generateEnemies(level,player)    
    for ammos in ammo:
        ammos.main(display)
    for sprite in all_sprites:
        sprite.main(display)
        sprite.update(GLOBAL_TIME,player)
    for enemy in enemies:
        enemy.moveToPlayer(player)
    clock.tick(60)
    
   
    
    # Score and timer rendering
    
    if timeSinceLevelStart >= timeToNextLevel:
        level += 1
        timeSinceLevelStart = 0
        timeToNextLevel += (100 + 10*level)
    
    f = pygame.font.SysFont("Verdana",20)
    g = f.render("Level: " + str(level),True,(255,255,255))
    display.blit(g,(400,10))
    
    p = f.render("Score: " + str(player.points),True,(255,255,255))
    display.blit(p,(600,10))
    
    a = f.render("Ammo: " + str(player.ammo),True,(255,255,255))
    display.blit(a,(100,10))
    
    # Game Over
    gameOver = player.gameOver
    if gameOver:
        time.sleep(2)
        for sprites in all_sprites:
            sprites.kill()
            display.fill((0,0,0))
            go = f.render(str("Game Over"),True,(255,255,255))
            display.blit(go,(320,200))
            p = f.render("Score: " + str(player.points),True,(255,255,255))
            display.blit(p,(320,250))
            g = f.render("Level: " + str(level),True,(255,255,255))
            display.blit(g,(320,300))
            pygame.display.update()
        time.sleep(1)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    
    
    
    