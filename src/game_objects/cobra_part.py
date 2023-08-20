from pygame import Surface, Vector2
from enum import Enum
from src.game_objects.game_tiles import Grass, Wall
from src.base.object import Object
from src.base.tile import Tile

HORIZONTAL_SNAKE_PART_SPRITE = Surface((1, 1))
VERCTICAL_SNAKE_PART_SPRITE = Surface((1, 1))
LEFT_TO_UP_SNAKE_PART_SPRITE = Surface((1, 1))
LEFT_TO_DOWN_SNAKE_PART_SPRITE = Surface((1, 1))
RIGHT_TO_UP_SNAKE_PART_SPRITE = Surface((1, 1))
RIGHT_TO_DOWN_SNAKE_PART_SPRITE = Surface((1, 1))

class Directions(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class CobraPart(Tile):
    """
    Class representing ever part of the cobra.
    Has the same functionality as a normal tile.
    Follows the start and end of the cobra and adjusts the
    sprite to it.

    Parameters:
    tile parameters;
    begin;
    end;
    """

    sprite_coordinates = {(Directions.UP, Directions.DOWN) : HORIZONTAL_SNAKE_PART_SPRITE,
                          (Directions.LEFT, Directions.UP) : LEFT_TO_UP_SNAKE_PART_SPRITE,
                          (Directions.LEFT, Directions.DOWN) : LEFT_TO_DOWN_SNAKE_PART_SPRITE,
                          (Directions.UP, Directions.DOWN) : HORIZONTAL_SNAKE_PART_SPRITE,
                          (Directions.RIGHT, Directions.UP) : RIGHT_TO_UP_SNAKE_PART_SPRITE,
                          (Directions.RIGHT, Directions.DOWN) : RIGHT_TO_DOWN_SNAKE_PART_SPRITE}


    def __init__(self,
                 coordinate_x: int = 0,
                 coordinate_y: int = 0) -> None:
        """
        Initialises the cobra part left to right.

        Sets:
        default tile parameters;
        begining of the cobra part;
        end of the cobra part;
        """
        super().__init__(coordinate_x, coordinate_y)
        self.begin: Directions = Directions.LEFT
        self.end: Directions = Directions.RIGHT
        self._set_sprite

    def are_valid_directions(self,
                               direction_begin: int = 1,
                               direction_end: int = 2) -> bool:
        """Checks if the directions are valid and returns the result"""
        if direction_begin > 4\
           or direction_end > 4\
           or direction_begin <= 0\
           or direction_end <= 0\
           or direction_end == direction_begin:
            return False

    def set_change_directions(self,
                              direction_begin: int = 1,
                              direction_end: int = 2) -> bool:
        """
        Changes the direction of the cobra part.
        1 for left
        2 for right
        3 for up
        4 for down
        """
        if not self.are_valid_directions(direction_begin, direction_end):
            return False
        self.begin = Directions(direction_begin)
        self.end = Directions(direction_end)
        self._set_sprite()
        return True

    def _set_sprite(self) -> None:
        """
        Sets the right sprite for the cobra part depending on the directions
        assuming the directions are right.
        """
        if CobraPart.sprite_coordinates.get((self.begin, self.end)):
            self.sprite = (self.begin, self.end)
        else:
            self.sprite = (self.end, self.begin)
