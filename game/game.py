import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacles = []

# Clock
clock = pygame.time.Clock()



pygame.display.flip()
clock.tick(60)

pygame.quit()
sys.exit()