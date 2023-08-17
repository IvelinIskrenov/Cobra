from pygame import Vector2, Surface, transform
from renderable_object import RenderableObject

SQUARE_WIDTH = 64
SQUARE_HEIGHT = 64
class Sqaure(RenderableObject):
    """
    Abstract class that presents the game squares.
    Squares have defined height and width, and are coordinate oriented.
    """
    def __init__(self,
                 sprite: Surface,
                 coordinate_x: int,
                 coordinate_y: int) -> None:
        """
        Initialises the game sqaure object.
        An abstract class that defines the game logic.
        Sets: position,
        sprite - (scales with width and height of the sqaure),
        visibility,
        coordinates: x and y - relative to other squares
        """
        self.x = coordinate_x
        self.y = coordinate_y
        square_position_x = self.x*SQUARE_WIDTH
        square_position_y = self.y*SQUARE_HEIGHT
        square_position = Vector2(square_position_x, square_position_y)
        super.__init__(square_position, sprite, True)
        self.sprite = transform.scale(self.sprite, (SQUARE_WIDTH, SQUARE_HEIGHT))
