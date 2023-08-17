import unittest
from base.square import Square, SQUARE_HEIGHT, SQUARE_WIDTH


class TestingSquare(unittest.TestCase):

    def test_square_initialisation(self):
        square1 = Square(0, 0)

        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)
        self.assertEqual(square1.position.x, 0)
        self.assertEqual(square1.position.y, 0)

    def test_square_relativity_to_other_squares(self):
        square1 = Square(0, 0)
        square2 = Square(1, 1)
        square3 = Square(2, 2)
        
        self.assertEqual(square1.position.x + SQUARE_WIDTH, square2.position.x)
        self.assertEqual(square1.position.y + SQUARE_HEIGHT, square2.position.y)

        self.assertEqual(square1.position.x + 2*SQUARE_WIDTH, square3.position.x)
        self.assertEqual(square1.position.y + 2*SQUARE_HEIGHT, square3.position.y)