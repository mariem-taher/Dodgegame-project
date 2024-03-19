import pygame
import random

pygame.init()

#creating the screen 

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DODGE GAME")

#setting colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#creating player

player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

#creating obstacle

obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacles = []

clock = pygame.time.Clock()

def create_obstacle():
    x = random.randint(0, screen_width - obstacle_width)
    y = 0
    obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))

def draw_player():
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height)) 

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, obstacle)

def move_obstacles():
    for obstacle in obstacles:
        obstacle.y = obstacle.y+obstacle_speed

def collision():
    for obstacle in obstacles:
        if obstacle.colliderect(player):
            return True
    return False
    
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    if random.randint(0, 100) < 3:
        create_obstacle()

    move_obstacles()
    draw_obstacles()

    player = pygame.Rect(player_x, player_y, player_width, player_height)
    draw_player()

    if collision():
        print("Game Over!")
        running = False

pygame.display.flip()
clock.tick(60)

pygame.quit()
