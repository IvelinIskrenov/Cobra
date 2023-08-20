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

    def test_cobra_part_change_directions(self):
        cobra_part = CobraPart()

        self.assertEqual(cobra_part.change_directions(1, 2), HORIZONTAL_SNAKE_PART_SPRITE)
        self.assertEqual(cobra_part.change_directions(1, 3), LEFT_TO_UP_SNAKE_PART_SPRITE)
        self.assertEqual(cobra_part.change_directions(2, 4), RIGHT_TO_DOWN_SNAKE_PART_SPRITE)
