from imports import *

pygame.init()

display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

    
player = Player(400,300,32,32)

# Enemy
E1 = Enemy(random.randrange(200,400),random.randrange(100,200))

display_scroll = [0,0]

all_sprites.add(player)
addEnemy(E1)

# Game loop
while True:
    dt = clock.tick()
    GLOBAL_TIME += dt
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
    eventHandler(keys,display_scroll,SPEED,non_player_sprites)
    pygame.draw.rect(display,(255,255,255),(100-display_scroll[0],100-display_scroll[1],16,16))
        
    player.main(display)
    
    for sprite in non_player_sprites:
        sprite.main(display)
        sprite.update(GLOBAL_TIME)
    
    clock.tick(60)
    pygame.display.update()
    
    