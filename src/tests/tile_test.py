from unittest import TestCase
from src.base.tile import Tile, SQUARE_HEIGHT, SQUARE_WIDTH


class TestingTile(TestCase):

    def test_tile_initialisation(self):
        tile1 = Tile(0, 0)

        self.assertEqual(tile1.x, 0)
        self.assertEqual(tile1.y, 0)
        self.assertEqual(tile1.position.x, 0)
        self.assertEqual(tile1.position.y, 0)

    def test_tile_relativity_to_other_tiles(self):
        tile1 = Tile(0, 0)
        tile2 = Tile(1, 1)
        tile3 = Tile(2, 2)
        
        self.assertEqual(tile1.position.x + SQUARE_WIDTH, tile2.position.x)
        self.assertEqual(tile1.position.y + SQUARE_HEIGHT, tile2.position.y)

        self.assertEqual(tile1.position.x + 2*SQUARE_WIDTH, tile3.position.x)
        self.assertEqual(tile1.position.y + 2*SQUARE_HEIGHT, tile3.position.y)
