import pytest
import pygame
from dodgegame import create_obstacle, move_obstacles, collision
#vérifie si la fonction crée un nouvel obstacle dans le jeu.
def test_create_obstacle():
    pygame.init()
    #compter le nombre d'obstacles présents avant l'appel à la methode
    obstacles_before = len(pygame.sprite.spritecollide(player, obstacles, False))
    create_obstacle()
    obstacles_after = len(pygame.sprite.spritecollide(player, obstacles, False))
    assert obstacles_after > obstacles_before
# vérifie si la fonction déplace les obstacles ou pas.
def test_move_obstacle():
    #les positions initiales en y de tous les obstacles sont enregistrées.
    initial_y_positions = [obstacle.y for obstacle in obstacles]
    move_obstacles()
    final_y_positions = [obstacle.y for obstacle in obstacles]
    #Le test vérifie si les positions finales sont différentes des positions initiales,ce qui signifie que les obstacles ont été déplacés.
    assert final_y_positions != initial_y_positions
#vérifie le comportement de la fonction:
def test_collision():
    pygame.init()
    #cas 1:
    player = pygame.Rect(0, 0, 50, 50)
    obstacles = [pygame.Rect(0, 0, 50, 50)] #on suppose que l'obstacle et le joueur entre en collision
    assert collision(player, obstacles) == True

    #cas 2:
    player = pygame.Rect(0, 0, 50, 50)
    obstacles = [pygame.Rect(100, 100, 50, 50)]  # on suppose que ces deux n'entrent pas en collision.
    assert collision(player, obstacles) == False
