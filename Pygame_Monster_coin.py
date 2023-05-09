import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escapa del Monstruo")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Definir fuente de texto
font = pygame.font.SysFont(None, 30)

# Definir variables globales
player_position = [SCREEN_WIDTH/2, SCREEN_HEIGHT-100]
player_size = 50
enemy_position = [random.randint(0, SCREEN_WIDTH-50), 0]
enemy_size = 50
coin_position = [random.randint(0, SCREEN_WIDTH-50), 0]
coin_size = 25
coin_list = []
for i in range(10):
    coin_list.append([random.randint(0, SCREEN_WIDTH-50), random.randint(0, SCREEN_HEIGHT-50)])
score = 0

# Función para dibujar el jugador
def draw_player(player_position):
    pygame.draw.rect(screen, YELLOW, [player_position[0], player_position[1], player_size, player_size])

# Función para mover el jugador
def move_player(player_position, key):
    if key == pygame.K_LEFT:
        player_position[0] -= 1
    elif key == pygame.K_RIGHT:
        player_position[0] += 1

# Función para dibujar el enemigo
def draw_enemy(enemy_position):
    pygame.draw.rect(screen, RED, [enemy_position[0], enemy_position[1], enemy_size, enemy_size])

# Función para mover el enemigo
def move_enemy(enemy_position):
    enemy_position[1] += 0.5

# Función para dibujar una moneda
def draw_coin(coin_position):
    pygame.draw.circle(screen, WHITE, coin_position, coin_size)

# Función para mover una moneda
def move_coin(coin_position):
    coin_position[1] += 0.1

# Función para detectar colisiones entre dos objetos
def collision_detection(rect1, rect2):
    if (rect1[1] + rect1[3] >= rect2[1]) and (rect1[1] <= rect2[1] + rect2[3]) and (rect1[0] + rect1[2] >= rect2[0]) and (rect1[0] <= rect2[0] + rect2[2]):
        return True
    else:
        return False

# Función para dibujar el puntaje
def draw_score(score):
    score_text = font.render("Puntaje: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

# Loop principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Limpiar pantalla
    screen.fill(BLACK)

    # Dibujar jugador
    draw_player(player_position)

      # Mover jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_player(player_position, pygame.K_LEFT)
    if keys[pygame.K_RIGHT]:
        move_player(player_position, pygame.K_RIGHT)

    # Dibujar enemigo
    draw_enemy(enemy_position)

    # Mover enemigo
    move_enemy(enemy_position)

    # Dibujar monedas
    for coin_pos in coin_list:
        draw_coin(coin_pos)

    # Mover monedas y detectar colisiones con jugador
    for i, coin_pos in enumerate(coin_list):
        move_coin(coin_pos)
        if collision_detection([player_position[0], player_position[1], player_size, player_size], [coin_pos[0], coin_pos[1], coin_size, coin_size]):
            coin_list[i] = [random.randint(0, SCREEN_WIDTH-50), 0]
            score += 10

    # Detectar colisión entre enemigo y jugador
    if collision_detection([player_position[0], player_position[1], player_size, player_size], [enemy_position[0], enemy_position[1], enemy_size, enemy_size]):
        game_over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text, [SCREEN_WIDTH/2 - 60, SCREEN_HEIGHT/2])
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    # Dibujar puntaje
    draw_score(score)

    # Actualizar pantalla
    pygame.display.update()

# Salir del juego
pygame.quit()

