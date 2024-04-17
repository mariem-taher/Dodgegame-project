import unittest
#to create patches for testing and mock objects, respectively:
from unittest.mock import patch, MagicMock
import sys
from io import StringIO

from dodgegame import *

class TestGame(unittest.TestCase):
    @patch('dodgegame.create_obstacle')
    def test_create_obstacle_called(self, mock_create_obstacle):
        create_obstacle()
        mock_create_obstacle.assert_called_once()
    #verifies that the patched create_obstacle function was called exactly once.
    @patch('dodgegame.random.randint', return_value=0)
    #decorates the test method and patches the random.randint function in the dodgegame module with a mock object (mock_randint) that always returns 0.
    def test_create_obstacle_position(self, mock_randint):
        create_obstacle()
        self.assertEqual(obstacles[-1].x, 0)
        self.assertEqual(obstacles[-1].y, 0)


if __name__ == "__main__":
    #checks if the script is being run directly
    unittest.main()
