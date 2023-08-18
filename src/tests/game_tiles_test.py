from unittest import TestCase
from src.game_objects.game_tiles import Grass, Wall

class TestingTile(TestCase):

    def test_grass_blockade(self):
        grass = Grass()
        self.assertFalse(grass.is_blockade())

    def test_wall_blockade(self):
        wall = Wall()
        self.assertTrue(wall.is_blockade())