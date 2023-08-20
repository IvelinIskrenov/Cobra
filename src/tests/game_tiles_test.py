from unittest import TestCase
from src.game_objects.game_tiles import Grass, Wall

class TestingTile(TestCase):

    def test_grass_cobra_obstruction(self):
        grass = Grass()
        self.assertFalse(grass.is_cobra_obstruction())

    def test_wall_cobra_obstruction(self):
        wall = Wall()
        self.assertTrue(wall.is_cobra_obstruction())
