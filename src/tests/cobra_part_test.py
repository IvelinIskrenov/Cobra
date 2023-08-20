from unittest import TestCase
from game_objects.cobra_part import *

class TestingCobraPart(TestCase):

    def test_cobra_test_directions(self):
        cobra_part = CobraPart()

        self.assertFalse(cobra_part.are_valid_directions(1, 1))
        self.assertTrue(cobra_part.are_valid_directions(1, 2))
        self.assertFalse(cobra_part.are_valid_directions(2, 2))
        self.assertTrue(cobra_part.are_valid_directions(2, 3))
        self.assertTrue(cobra_part.are_valid_directions(3, 1))
        self.assertFalse(cobra_part.are_valid_directions(4, 4))
