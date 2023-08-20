from pygame import Surface
from src.game_objects.cobra_part import CobraPart, Directions
from src.base.tile import Tile

class CobraHead(CobraPart):
    def __init__(self,
                 coordinate_x: int = 0,
                 coordinate_y: int = 0) -> None:
        super().__init__(coordinate_x, coordinate_y)



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
        self.facing: Directions = Directions.RIGHT
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
        Moves the snake around.
        Essentially works as a queue, every part follows the one before it.
        """
        if not self.active:
            return
        old_part = self.parts[0]
        if self.facing == Directions.RIGHT:
            self.parts[0].set_coordinates(old_part.x + 1, old_part.y, self.offset_x, self.offset_y)
        if self.facing == Directions.LEFT:
            self.parts[0].set_coordinates(old_part.x - 1, old_part.y, self.offset_x, self.offset_y)
        if self.facing == Directions.UP:
            self.parts[0].set_coordinates(old_part.x, old_part.y - 1, self.offset_x, self.offset_y)
        if self.facing == Directions.DOWN:
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

    def deactivate(self):
        """Deactivates the snake so it can't move."""
        self.active = False

    def activate(self):
        """Activates the snake so it can move."""
        self.active = True
