from pygame import Vector2, Surface
from src.base.tile import Tile


class Grass(Tile):
    """
    Grass tile for the cobra to move on. Uses the Tile interface.
    Not a blockade for the cobra.

    Parameters:
    coordinates;
    position;
    sprite;
    visibility.
    """
    def __init__(self,
                 coordinate_x: int = 0,
                 coordinate_y: int = 0) -> None:
        """Initialises the Grass Tile with the given coordinates.

        Sets:
        coordinates: x and y - relative to other tiles;
        position relative to the screen;
        default grass sprite;
        visibility.
        """
        super().__init__(coordinate_x, coordinate_y)

    def is_cobra_obstruction(self) -> bool:
        """Returns if the object is a blockade for the cobra or not"""
        return False

    def tile_to_str(self) -> str:
        return "G"


class Wall(Tile):
    """
    Wall tile for the cobra to collide with. Uses the Tile interface.
    A blockade for the cobra.

    Parameters:
    coordinates;
    position;
    sprite;
    visibility.
    """
    def __init__(self,
                 coordinate_x: int = 0,
                 coordinate_y: int = 0) -> None:
        """Initialises the Wall Tile with the given coordinates.

        Sets:
        coordinates: x and y - relative to other tiles;
        position relative to the screen;
        default wall sprite;
        visibility.
        """
        super().__init__(coordinate_x, coordinate_y)

    def is_cobra_obstruction(self) -> bool:
        """Returns if the object is a blockade for the cobra or not"""
        return True

    def tile_to_str(self) -> str:
        return "W"
