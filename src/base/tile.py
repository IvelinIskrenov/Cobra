from pygame import Vector2, Surface, transform
from src.base.renderable_object import RenderableObject

SQUARE_WIDTH = 64
SQUARE_HEIGHT = 64
class Tile(RenderableObject):
    """
    Abstract class that presents the game tiles.
    Tiles have defined height and width, and are coordinate oriented.

    Parameters:
    position;
    sprite;
    visibility;
    coordinates: x and y - relative to other tiles.
    """
    def __init__(self,
                 coordinate_x: int = 0,
                 coordinate_y: int = 0,
                 sprite: Surface = Surface((1,1))) -> None:
        """
        Initialises the game tile object.

        Sets:
        position - relative to the screen;
        sprite - (scales with width and height of the tile);
        visibility;
        coordinates: x and y - relative to other tiles.
        """
        super().__init__(sprite, Vector2(0, 0), True)
        self.set_coordinates(coordinate_x, coordinate_y)
        self.sprite = transform.scale(self.sprite, (SQUARE_WIDTH, SQUARE_HEIGHT))

    def is_snake_obstruction(self) -> bool:
        """Tells if the object is a blockade for the snake or not"""
        pass

    def set_coordinates(self,
                        coordinate_x: int,
                        coordinate_y: int,
                        offset_x: int = 0,
                        offset_y: int = 0) -> None:
        """
        Changes the coordinates of the tile relative to other tiles.
        Adds offset if needed.
        """
        self.x: int = coordinate_x
        self.y: int = coordinate_y
        tile_position_x = self.x*SQUARE_WIDTH + offset_x
        tile_position_y = self.y*SQUARE_HEIGHT + offset_y
        self.position = Vector2(tile_position_x, tile_position_y)