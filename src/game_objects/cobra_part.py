from os import path
from pygame import Surface, image, transform, Vector2
from enum import Enum
from src.base.tile import Tile

HORIZONTAL_SNAKE_PART_SPRITE =\
    image.load(path.join('src', 'sprites', 'half_cobra_straight_part.png'))
VERCTICAL_SNAKE_PART_SPRITE = transform.rotate(
    image.load(path.join('src', 'sprites', 'half_cobra_straight_part.png')), -90)
LEFT_TO_UP_SNAKE_PART_SPRITE =\
    image.load(path.join('src', 'sprites', 'left_to_up_cobra_part.png'))
LEFT_TO_DOWN_SNAKE_PART_SPRITE = transform.rotate(
    image.load(path.join('src', 'sprites', 'left_to_up_cobra_part.png'), 90))
RIGHT_TO_UP_SNAKE_PART_SPRITE = transform.rotate(
    image.load(path.join('src', 'sprites', 'left_to_up_cobra_part.png'), -90))
RIGHT_TO_DOWN_SNAKE_PART_SPRITE = transform.rotate(
    image.load(path.join('src', 'sprites', 'left_to_up_cobra_part.png'), 180))

class Direction(Enum):
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

    sprite_coordinates = {(Direction.LEFT, Direction.RIGHT) : VERCTICAL_SNAKE_PART_SPRITE,
                          (Direction.UP, Direction.DOWN) : HORIZONTAL_SNAKE_PART_SPRITE,
                          (Direction.LEFT, Direction.UP) : LEFT_TO_UP_SNAKE_PART_SPRITE,
                          (Direction.LEFT, Direction.DOWN) : LEFT_TO_DOWN_SNAKE_PART_SPRITE,
                          (Direction.UP, Direction.DOWN) : HORIZONTAL_SNAKE_PART_SPRITE,
                          (Direction.RIGHT, Direction.UP) : RIGHT_TO_UP_SNAKE_PART_SPRITE,
                          (Direction.RIGHT, Direction.DOWN) : RIGHT_TO_DOWN_SNAKE_PART_SPRITE}


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
        self.begin: Direction = Direction.LEFT
        self.end: Direction = Direction.RIGHT
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
        return True

    def change_directions(self,
                          direction_begin: int = 1,
                          direction_end: int = 2) -> bool:
        """
        Changes the direction of the cobra part.
        1 - left;
        2 - right;
        3 - up;
        4 - down.
        """
        if not self.are_valid_directions(direction_begin, direction_end):
            return False
        self.begin = Direction(direction_begin)
        self.end = Direction(direction_end)
        self._set_sprite()
        return True

    def _set_sprite(self) -> None:
        """
        Sets the right sprite for the cobra part depending on the directions
        assuming the directions are right.
        """
        if CobraPart.sprite_coordinates.get((self.begin, self.end)):
            self.sprite = CobraPart.sprite_coordinates.get((self.begin, self.end))
        else:
            self.sprite = CobraPart.sprite_coordinates.get((self.end, self.begin))

    def _is_horizontal_piece(self):
        """Checks whether the cobra piece is currently horizontal."""
        return self.begin in [Direction.LEFT, Direction.RIGHT]\
                and self.end in [Direction.LEFT, Direction.RIGHT]

    def _is_vertical_piece(self):
        """Checks whether the cobra piece is currently horizontal."""
        return self.begin in [Direction.UP, Direction.DOWN]\
                and self.end in [Direction.UP, Direction.DOWN]

    def _render_horizontal_piece(self, display: Surface):
        """
        Renders the entire horizontal cobra piece.
        """
        display.blit(self.sprite, self.position)
        half_piece_pos = self.position
        half_piece_pos.x += self.width/2
        display.blit(self.sprite, half_piece_pos)

    def _render_vertical_piece(self, display: Surface):
        """
        Renders the entire horizontal cobra piece.
        """
        display.blit(self.sprite, self.position)
        half_piece_pos = self.position
        half_piece_pos.y += self.height/2
        display.blit(self.sprite, half_piece_pos)

    def render_entire_part(self, display: Surface) -> None:
        """
        if visible, renders the entire cobra part, not only half of it.
        """
        if self.visible:
            if self._is_horizontal_piece():
                self._render_horizontal_piece(display)
            elif self._is_vertical_piece():
                self._render_vertical_piece(display)
            else:
                # this is in the case which the this is piece which is
                # responsible for turning the cobra
                self.render()

