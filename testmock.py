import unittest
#pour la création de patchs et d'objets lors du test.
from unittest.mock import patch, MagicMock
#pour l'accès à des variables et fonctions spécifiques au système:
import sys
#pour la création de flux de chaînes de caractères:
from io import StringIO
from dodgegame import *
#creation d'une classe qui fournit les fonctionnalités nécessaires pour écrire des tests unitaires
class TestGame(unittest.TestCase):
    #Ce test vérifie si la fonction est appelée une seule fois ou non
    @patch('dodgegame.create_obstacle')
    #on patche avec un objet fictif (mock_create_obstacle) pour vérifier si elle est appelée.
    def test_create_obstacle_called(self, mock_create_obstacle):
        create_obstacle()
        #on vérifie si cet objet a été appelée exctement une seule fois 
        mock_create_obstacle.assert_called_once()

    #Ce test vérifie si la position de l'obstacle créé est correcte:
    @patch('dodgegame.random.randint', return_value=0)#patchée avec un retour a la valeur 0
    #decorates the test method and patches the random.randint function in the dodgegame module with a mock object (mock_randint) that always returns 0.
    def test_create_obstacle_position(self, mock_randint):
        create_obstacle()
        self.assertEqual(obstacles[-1].x, 0)
        self.assertEqual(obstacles[-1].y, 0)
    #on vérifie si les coordonnées x et y ,du dernier obstacle, sont égales à 0


if __name__ == "__main__":
    #verifie si le script est executé directement 
    unittest.main()
