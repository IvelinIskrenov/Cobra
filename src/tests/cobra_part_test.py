from unittest import TestCase
from game_objects.cobra_part import *

class TestingCobraPart(TestCase):

    def test_cobra_part_change_directions(self):
        cobra_part = CobraPart()

        self.assertTrue(cobra_part.are_valid_directions(1, 1))
        self.assertTrue(cobra_part.are_valid_directions(1, 2))
        self.assertTrue(cobra_part.are_valid_directions(2, 2))
