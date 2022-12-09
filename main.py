from imports import *
# import os
from pygame import KEYDOWN

# os.add_dll_directory('C:\Windows\System32\libmpg123-0.dll')
# from playsound import playsound
# import threading
file = 'futuristic-timelapse-11951.mp3'
pygame.init()

# Music (Currently Broken)
pygame.mixer.music.load(file)
    # Threading, temp fix
# threading.Thread(target=playsound, args=(file,), daemon=True).start()




def gameInit(menu = True):
    display = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    player = Player(400,300,32,32)
    all_sprites.add(player)
    if menu:
        startMenu(display,clock,player)
    else:
        main(clock,player,display)
# Game loop
def main(clock,player,display):
    pygame.mixer.music.play(loops = 1) # BG Music
    gameOver = False
    timeToNextLevel = 300
    display_scroll = [0,0]
    timeSinceLevelStart = 0
    GLOBAL_TIME = 0
    level = 1
    do_once = 0
    while True:
        gameOver = False
        dt = clock.tick()
        GLOBAL_TIME += dt
        timeSinceLevelStart += dt
        display.fill((14,65,33)) # Background color
        
        mouse_x,mouse_y = pygame.mouse.get_pos()
        
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not gameOver:
                    bullet = PlayerBullet(player.x+16,player.y+16,mouse_x,mouse_y,GLOBAL_TIME)
                    addBullet(bullet)
                if event.button == 3 and not gameOver:
                    shotgun(player, mouse_x,mouse_y,GLOBAL_TIME)
            if event.type == KEYDOWN:
                if event.key == pygame.K_r:
                    for sprite in all_sprites:
                        sprite.kill()
                    gameInit(False)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:
                    gameInit(True)
                    
        # Movement
        keys = pygame.key.get_pressed()
        controller(keys,display_scroll,SPEED,non_player_sprites)
        # Enemy generation and movement 
        # threading.Thread(target = generateEnemies, args = (level,player), daemon = False).start()
        generateEnemies(level,player)    
        for ammos in ammo:
            ammos.main(display)
        for sprite in all_sprites:
            sprite.main(display)
            sprite.update(GLOBAL_TIME,player)
        for enemy in enemies:
            enemy.moveToPlayer(player)
        clock.tick(60)
        # HUD
        if (timeSinceLevelStart >= timeToNextLevel) and not gameOver:
            level += 1
            timeSinceLevelStart = 0
            timeToNextLevel += (100 + 10*level)
        
        f = pygame.font.SysFont("Verdana",20)
        f1 = pygame.font.SysFont("Verdana",34)
        HUD(display,f,level,player)
        
        # Game Over
        gameOver = player.gameOver
        if gameOver:
            if do_once == 0:
                time.sleep(1)
                finalLevel = level
                do_once += 1
            for sprites in all_sprites:
                sprites.kill()
                gameOverScreen(display,finalLevel,player,f,f1)
            pygame.display.update()
            

        pygame.display.update()   

def gameOverScreen(display,finalLevel,player,f,f1):
    display.fill((0,0,0))
    go = f1.render(str("Game Over"),True,(255,255,255))
    display.blit(go,(300,170))
    p = f.render("Score: " + str(player.points),True,(255,255,255))
    display.blit(p,(320,240))
    g = f.render("Level: " + str(finalLevel),True,(255,255,255))
    display.blit(g,(320,280))
    restartText1 = f.render("Retry (r)",True,(255,255,255))
    display.blit(restartText1,(260,335))
    restartText2 = f.render("Quit (ESC)",True,(255,255,255))
    display.blit(restartText2,(380,335))
    mainMenuText = f.render("Menu (m)",True,(255,255,255))
    display.blit(mainMenuText,(320,430))
    
def startMenu(display,clock,player):
    display.fill((0,0,0))
    f = pygame.font.SysFont("Verdana",20)
    while True:
        start = f.render("Press (s) to start",True,(255,255,255))
        display.blit(start,(220,170))
        quit = f.render("Press (ESC) to quit",True,(255,255,255))
        display.blit(quit,(220,200))
        controls = f.render("Press (c) to view the controls",True,(255,255,255))
        display.blit(controls,(220,260))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    main(clock,player,display)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_c:
                    Controls(display,f)
def Controls(display,f):
    display.fill((0,0,0))
    controlsString1 = "Use WASD to move around"
    controlsString2 = "Use the left mouse button to fire"
    controlsString3 = "Use the right mouse button to shoot your shotgun"
    while True:
        CSR1 = f.render(controlsString1,True,(255,255,255))
        CSR2 = f.render(controlsString2,True,(255,255,255))
        CSR3 = f.render(controlsString3,True,(255,255,255))
        returnString = f.render('Press (m) to return to the menu',True,(255,255,255))
        display.blit(returnString,(200,500))
        display.blit(CSR1,(200,200))
        display.blit(CSR2,(200,250))
        display.blit(CSR3,(200,300))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    gameInit(True)
        pygame.display.update()
        
def HUD(display,f,level,player):
    g = f.render("Level: " + str(level),True,(255,255,255))
    display.blit(g,(350,10))
    
    p = f.render("Score: " + str(player.points),True,(255,255,255))
    display.blit(p,(685,10))
    
    a = f.render("Ammo: " + str(player.ammo),True,(255,255,255))
    display.blit(a,(10,10))
gameInit(True)    
    