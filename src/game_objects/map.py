from pygame import Vector2
from src.game_objects.game_tiles import Grass, Wall
from src.base.object import Object
from src.base.tile import Tile
class Map(Object):
    """
    Object that holds information about the tiles.

    Parameters:
    position - relative to the screen;
    tiles - array of arrays of tiles.
    rows;
    coulmns.
    """
    def __init__(self,
                 rows: int = 10,
                 columns: int = 10,
                 position: Vector2 = (0,0)) -> None:
        """
        Initialises the map with tiles with sizes rows and columns.

        Sets:
        position;
        rows;
        coulmns.
        """
        super().__init__(position)
        self.rows: int = rows
        self.columns: int = columns
        self.tiles: list[list[Tile]] = ([Tile()]*columns)*rows



