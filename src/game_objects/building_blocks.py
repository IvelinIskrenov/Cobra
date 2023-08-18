from pygame import Vector2, Surface
from src.base.tile import Tile


class Grass(Tile):
    """
    Grass tile for the snake to move on. Uses the Tile interface.
    Not a blockade for the snake.
    Sets:
    Coordinates relative to the field,
    Default grass sprite
    """
    def __init__(coordinate_x: int = 0,
                 coordinate_y: int = 0):
        super().__init__(coordinate_x, coordinate_y, Surface())
    
    def is_blockade():
        return False
    

class Wall(Tile):
     """
    Wall tile for the snake to move on. Uses the Tile interface.
    Not a blockade for the snake.
    Sets:
    Coordinates relative to the field,
    Default grass sprite
    """
    def __init__(coordinate_x: int = 0,
                 coordinate_y: int = 0):
        super().__init__(coordinate_x, coordinate_y, Surface())
    
    def is_blockade():
        return True