import pytest
import pygame
from dodgegame import create_obstacle, move_obstacles, collision

def test_create_obstacle():
    pygame.init()
    obstacles_before = len(pygame.sprite.spritecollide(player, obstacles, False))
    create_obstacle()
    obstacles_after = len(pygame.sprite.spritecollide(player, obstacles, False))
    assert obstacles_after > obstacles_before

def test_move_obstacle():
    initial_y_positions = [obstacle.y for obstacle in obstacles]
    move_obstacles()
    final_y_positions = [obstacle.y for obstacle in obstacles]
    assert final_y_positions != initial_y_positions

def test_collision():
    pygame.init()
    player = pygame.Rect(0, 0, 50, 50)
    obstacles = [pygame.Rect(0, 0, 50, 50)]  # Assuming the obstacle collides with the player
    assert collision(player, obstacles) == True

    player = pygame.Rect(0, 0, 50, 50)
    obstacles = [pygame.Rect(100, 100, 50, 50)]  # Assuming the obstacle doesn't collide with the player
    assert collision(player, obstacles) == False

