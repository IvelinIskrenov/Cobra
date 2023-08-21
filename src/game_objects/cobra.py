from os import path
from pygame import Surface, image, transform
from src.game_objects.cobra_part import CobraPart, Direction
from src.base.tile import Tile

COBRA_HEAD_SPRITE = \
    image.load(path.join('src', 'sprites', 'cobra_head.png'))

class CobraHead(CobraPart):
    """
    Essentially the same class as the cobra part but
    has a head sprite instead and rotates differently.
    """
    def __init__(self,
                 coordinate_x: int = 0,
                 coordinate_y: int = 0) -> None:
        """Initialises the head and places the head sprite"""
        super().__init__(coordinate_x, coordinate_y)
        self.sprite = COBRA_HEAD_SPRITE

    def change_directions(self,
                          direction_begin: int = 1,
                          direction_end: int = 2) -> bool:
        """
        Changes the direction of the head and places the
        sprite needed to represent where the head is looking
        """
        if not self.are_valid_directions():
            return False
        self.begin = Direction(direction_begin)
        self.end = Direction(direction_end)
        self._change_sprite()

    def _change_sprite(self)-> None:
        """Sets the sprite to look at the end direction of the cobra head"""
        if self.end == Direction.RIGHT:
            self.sprite = COBRA_HEAD_SPRITE
        elif self.end == Direction.LEFT:
            self.sprite = transform.rotate(COBRA_HEAD_SPRITE, 180)
        elif self.end == Direction.UP:
            self.sprite = transform.rotate(COBRA_HEAD_SPRITE, 90)
        elif self.end == Direction.RIGHT:
            self.sprite = transform.rotate(COBRA_HEAD_SPRITE, -90)


    def render_head(display):
        """Renders the head of the cobra"""

class Cobra():
    """
    Cobra class that colds the cobra parts information
    and can move the cobra parts around,
    essentially representing actual cobra.

    Parameters:
    parts - cobra parts;
    facing - direction of cobra;
    eaten - has it eaten since last step;
    active - is it moving.
    """
    def __init__(self,
                 start_coordinate_x: int = 2,
                 start_coordinate_y: int = 2,
                 offset_x: int = 0,
                 offset_y: int = 0) -> None:
        """
        Initialises the cobra parts.

        Sets:
        parts - only head and one part;
        facing - right;
        eaten;
        active;
        """
        self.parts: list[CobraPart] = []
        self.facing: Direction = Direction.RIGHT
        self.offset_x: int = offset_x
        self.offset_y: int = offset_y
        self.eaten = False
        self.active = True
        self.parts.append(CobraHead())
        self.parts.append(CobraPart())
        self.parts[0].set_coordinates(start_coordinate_x, start_coordinate_y, offset_x, offset_y)
        self.parts[1].set_coordinates(start_coordinate_x - 1, start_coordinate_y, offset_x, offset_y)

    def next_step(self) -> None:
        """
        Moves the cobra around.
        Essentially works as a queue, every part follows the one before it.
        """
        if not self.active:
            return
        old_part = self.parts[0]
        if self.facing == Direction.RIGHT:
            self.parts[0].set_coordinates(old_part.x + 1, old_part.y, self.offset_x, self.offset_y)
        if self.facing == Direction.LEFT:
            self.parts[0].set_coordinates(old_part.x - 1, old_part.y, self.offset_x, self.offset_y)
        if self.facing == Direction.UP:
            self.parts[0].set_coordinates(old_part.x, old_part.y - 1, self.offset_x, self.offset_y)
        if self.facing == Direction.DOWN:
            self.parts[0].set_coordinates(old_part.x, old_part.y + 1, self.offset_x, self.offset_y)
        for part in self.parts:
            old_part_buffer = part
            part.set_coordinates(old_part.x, old_part.y, self.offset_x, self.offset_y)
            part.change_directions(old_part.begin, old_part.end)
            old_part = old_part_buffer
        if self.eaten:
            self.eaten = False
            self.parts.append(CobraPart())
            self.parts[-1].change_directions(old_part.begin, old_part.end)
            self.parts[-1].set_coordinates(old_part.x, old_part.y, self.offset_x, self.offset_y)

    def get_head_position(self) -> tuple[int, int]:
        """Returns the head's position relative to the tiles."""
        return (self.parts[0].x, self.parts[0].y)

    def render(self, display: Surface) -> None:
        """Renders the entire cobra on the given display"""
        for cobra_part in self.parts[1:-1]:
            cobra_part.render_entire_part(display)
        # the head of the cobra has other method of rendering.
        self.parts[0].render_head(display)

    def deactivate(self):
        """Deactivates the cobra so it can't move."""
        self.active = False

    def activate(self):
        """Activates the cobra so it can move."""
        self.active = True
