from os import path
from pygame import Surface, image, transform
from src.game_objects.cobra_part import CobraPart, Direction

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


    def render_head(self, display: Surface):
        """Renders the head of the cobra"""
        super().render(display)

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
        self.head = CobraHead()
        self.parts: list[CobraPart] = [CobraPart()]
        self.facing: Direction = Direction.RIGHT
        self.next_direction: Direction = Direction.RIGHT
        self.offset_x: int = offset_x
        self.offset_y: int = offset_y
        self.eaten = False
        self.active = True
        self.head.set_coordinates(start_coordinate_x, start_coordinate_y, offset_x, offset_y)
        self.parts[0].set_coordinates(start_coordinate_x - 1, start_coordinate_y, offset_x, offset_y)

    def get_next_head_coordinates(self) -> tuple[int, int]:
        """Returns where the head would move next depending on the next direction"""
        if self.next_direction == Direction.RIGHT:
            return (self.head.x + 1, self.head.y)
        if self.next_direction == Direction.LEFT:
            return (self.head.x - 1, self.head.y)
        if self.next_direction == Direction.UP:
            return (self.head.x, self.head.y + 1)
        if self.next_direction == Direction.DOWN:
            return (self.head.x, self.head.y - 1)

    def next_step(self) -> None:
        """
        Moves the cobra around.
        Essentially works as a queue, every part follows the one before it.
        """
        if not self.active:
            return
        old_coordinates = (self.head.x, self.head.y)
        old_directions = (self.head.begin, self.next_direction)
        next_coordinates = self.get_next_head_coordinates()
        self.head.set_coordinates(next_coordinates[0], next_coordinates[1], self.offset_x, self.offset_y)

        self.head.begin = self.head.get_opposite_direction(self.next_direction)
        self.head.end = self.next_direction

        for part in self.parts:
            old_coordinates_buffer = (part.x, part.y)
            old_directions_buffer = (part.begin, part.end)
            part.set_coordinates(old_coordinates[0], old_coordinates[1], self.offset_x, self.offset_y)
            part.change_directions(old_directions[0], old_directions[1])
            old_coordinates = old_coordinates_buffer
            old_directions = old_directions_buffer
        if self.eaten:
            self.eaten = False
            self.parts.append(CobraPart())
            self.parts[-1].change_directions(old_directions[0], old_directions[1])
            self.parts[-1].set_coordinates(old_coordinates[0], old_coordinates[1], self.offset_x, self.offset_y)

    def get_head_position(self) -> tuple[int, int]:
        """Returns the head's position relative to the tiles."""
        return (self.head.x, self.head.y)

    def render(self, display: Surface) -> None:
        """Renders the entire cobra on the given display"""
        for cobra_part in self.parts:
            cobra_part.render_entire_part(display)
        # the head of the cobra has other method of rendering.
        self.head.render_head(display)

    def switch_direction_to_input(self, input: int) -> bool:
        """
        Changes the direction of the cobra in the next move.
        1 - left;
        2 - right;
        3 - up;
        4 - down.
        Returns false if not changed, true otherwise.
        """
        if not self.head.is_valid_direction(input):
            return False
        needed_direction = Direction(input)
        if self.head.get_opposite_direction(self.facing)\
            == needed_direction:
            return False
        self._change_next_direction(needed_direction)


    def _change_next_direction(self, direction: Direction) -> None:
        """Changes the next direction of the cobra so it can rotate on the next step."""
        self.next_direction = direction

    def deactivate(self):
        """Deactivates the cobra so it can't move."""
        self.active = False

    def activate(self):
        """Activates the cobra so it can move."""
        self.active = True
