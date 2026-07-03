import pygame
import random

pygame.init()

WIDTH = 900
HEIGHT = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('JOGO DO TREX')

clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = "green"
BLUE = "blue"

GROUND = HEIGHT - 50

player = pygame.Rect(80, GROUND - 55, 40, 60)

gravity = 0
jump = False

obstacles = []
speed = 7
score = 0

font = pygame.font.SysFont("arial", 28)

spawn_timer = 0

run = True

while run:
    clock.tick(60)

    screen.fill("white")

    pygame.draw.line(screen, BLUE, (0, GROUND), (WIDTH, GROUND), 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE, pygame.K_UP]:
                if not jump:
                    gravity = -15
                    jump = True

    gravity += 0.8
    player.y += int(gravity)

    if player.bottom >= GROUND:
        player.bottom = GROUND
        gravity = 0
        jump = False

    # Obstáculos
    spawn_timer += 1

    if spawn_timer > random.randint(50, 90):
        h = random.randint(40, 70)

        obstacle = pygame.Rect(
            WIDTH,
            GROUND - h,
            25,
            h
        )

        obstacles.append(obstacle)
        spawn_timer = 0

    for obstacle in obstacles[:]:
        obstacle.x -= speed

        if obstacle.right < 0:
            obstacles.remove(obstacle)
            score += 1

        if player.colliderect(obstacle):
            run = False

    # Aumentar dificuldade
    speed = 8 + score // 8

    # Jogador
    pygame.draw.rect(screen, GREEN, player)

    # Obstáculos
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    # Pontuação
    text = font.render(f"Pontos: {score}", True, BLUE)
    screen.blit(text, (20, 20))

    pygame.display.flip()

pygame.quit()

print("GAME OVER")
print(f"Pontuação final: {score}")