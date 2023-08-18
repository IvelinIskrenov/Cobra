from unittest import TestCase
from src.game_objects.game_tiles import Grass, Wall

class TestingTile(TestCase):

    def test_grass_snake_obstruction(self):
        grass = Grass()
        self.assertFalse(grass.is_snake_obstruction())

    def test_wall_snake_obstruction(self):
        wall = Wall()
        self.assertTrue(wall.is_snake_obstruction())
