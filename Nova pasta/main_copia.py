import pygame
import random

pygame.init()

WIDTH = 900
HEIGHT = 300

screen =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JOGO DO TREX')

GROUND = 230

# IMAGENS CARREGAR:
dino = pygame.image.load('1.png').convert_alpha()
dino2 = pygame.image.load('3.png').convert_alpha()
# dino3 = pygame.image.load('3.png').convert_alpha()
ground = pygame.image.load('ground2.png').convert_alpha()
cactus = pygame.image.load('obstacle1.png').convert_alpha()

dino = pygame.transform.scale(dino, (70,60))
dino2 = pygame.transform.scale(dino2, (70,60))
# dino3 = pygame.transform.scale(dino3, (30,60))
cactus = pygame.transform.scale(cactus, (30,60))

# animação
dino_frame2 = pygame.transform.flip(dino, True, False)
dino_frames = [dino,dino2, dino_frame2]
dino_index = 0

ground_x =  0

player = dino.get_rect()
player.x = 80
player.y = GROUND - 60
velocity = 0
jump = False

obstacles = []

speed = 8
score  = 0
font =  pygame.font.SysFont('arial', 28)

spawn_timer = 0
animation_timer = 0
run =  True
clock =  pygame.time.Clock()


while run:
    clock.tick(60)
    screen.fill('white')
   
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            run =  False

        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE, pygame.K_UP] and not jump:
                 velocity = -12
                 jump = True  

    velocity += 0.7
    player.y += velocity    
   
    if player.bottom >= GROUND:
        player.bottom = GROUND
        velocity = 0
        jump = False                    


    if not jump:
        animation_timer += 1
        if animation_timer > 10:
            animation_timer = 0
            dino_index = 1 - dino_index
            dino = dino_frames[dino_index]
        elif    animation_timer >= 15 and animation_timer <=20:
            animation_timer = 15
            dino_index = 1 + dino_index
            dino1 = dino_frames[dino_index]

        else:
            dino2   = dino_frames[dino_index]


           

           

    spawn_timer += 1
    if spawn_timer > 70:
       rect = cactus.get_rect()
       rect.x =  WIDTH
       rect.bottom=GROUND
       obstacles.append(rect)
       spawn_timer = random.randint(0,20)
   
    for obstacle in obstacles[:]:
        obstacle.x  -= speed

        # colisão
        if obstacle.right < 0 :
            obstacles.remove(obstacle)
            score += 1  
        if player.colliderect(obstacle):
            run = False
           
    # aumentar dificuldade
    speed = 8 + score // 8

    ground_x  -= speed
    if ground_x <= -ground.get_width():
        ground_x = 0


    screen.blit(ground, (ground_x, GROUND))
    screen.blit(ground, (ground_x+ground.get_width(), GROUND ))    

    screen.blit(dino, player)

    for obs in obstacles:
        screen.blit(cactus, obs)

    text =  font.render(f'Pontos {score}', True, 'blue')
    screen.blit(text, (20,20))    

    pygame.display.flip()

pygame.quit()
print('GAME OVER PONTUAÇÃO', score)