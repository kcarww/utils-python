import pygame
import random

# Inicialização do pygame
pygame.init()

# Dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Dimensões e posições iniciais
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 7

player_x, player_y = 10, (HEIGHT // 2) - (PADDLE_HEIGHT // 2)
opponent_x, opponent_y = WIDTH - 20, (HEIGHT // 2) - (PADDLE_HEIGHT // 2)
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

# Velocidades
player_speed = 0
opponent_speed = 7
ball_speed_x = 4 * random.choice((-1, 1))
ball_speed_y = 4 * random.choice((-1, 1))

# Placar
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)

# Função para desenhar a tela
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (opponent_x, opponent_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    player_text = font.render(f"{player_score}", True, WHITE)
    opponent_text = font.render(f"{opponent_score}", True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(opponent_text, (WIDTH * 3 // 4, 20))

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -7
            if event.key == pygame.K_DOWN:
                player_speed = 7
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player_speed = 0

    # Movimento do jogador
    player_y += player_speed
    if player_y < 0:
        player_y = 0
    if player_y > HEIGHT - PADDLE_HEIGHT:
        player_y = HEIGHT - PADDLE_HEIGHT

    # Movimento do oponente (simples IA)
    if opponent_y + (PADDLE_HEIGHT // 2) < ball_y:
        opponent_y += opponent_speed
    if opponent_y + (PADDLE_HEIGHT // 2) > ball_y:
        opponent_y -= opponent_speed
    if opponent_y < 0:
        opponent_y = 0
    if opponent_y > HEIGHT - PADDLE_HEIGHT:
        opponent_y = HEIGHT - PADDLE_HEIGHT

    # Movimento da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisão com a parede superior/inferior
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_speed_y *= -1

    # Colisão com o jogador
    if (player_x < ball_x - BALL_RADIUS < player_x + PADDLE_WIDTH and
            player_y < ball_y < player_y + PADDLE_HEIGHT):
        ball_speed_x *= -1

    # Colisão com o oponente
    if (opponent_x < ball_x + BALL_RADIUS < opponent_x + PADDLE_WIDTH and
            opponent_y < ball_y < opponent_y + PADDLE_HEIGHT):
        ball_speed_x *= -1

    # Pontuação
    if ball_x - BALL_RADIUS <= 0:
        opponent_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= random.choice((-1, 1))
        ball_speed_y *= random.choice((-1, 1))
    if ball_x + BALL_RADIUS >= WIDTH:
        player_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= random.choice((-1, 1))
        ball_speed_y *= random.choice((-1, 1))

    # Desenhar tudo
    draw()
    
    # Atualizar a tela
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
