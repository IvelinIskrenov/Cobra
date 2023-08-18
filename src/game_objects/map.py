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

    def _dfs_check( self,
                    i: int,
                    j: int,
                    visited: list[list[bool]]) -> str:
        """
        Given tile coordinates on the map:
        Checks if the map is valid with depth first search.
        Returns "valid" if yes.
        if no - returns:
        "not_SCC" if the component is not strongly connected,
        since the snake won't be able to go both ways.
        "out_of_bounds" if the snake can get out of the map.
        """
        if i<0 or i>=self.rows or j<0 or j>=self.columns:
            return "out_of_bounds"
        if visited[i][j]:
            return "valid"
        if self.tiles[i][j].is_snake_obstruction():
            visited[i][j] = True
            return "valid"
        
        directions = [1, -1]

        for direction in directions:
            result = self._dfs_check(i + direction)
            if result != "valid":
                return result
            result2 = self._dfs_check(j + direction)
            if result != "valid":
                return result

        for direction_x in directions:
            for direction_y in directions:
                i_new = i + direction_x
                j_new = j + direction_y
                if not\
                    (self.tiles[i_new][j_new].is_snake_obstruction()\
                    or self.tiles[i][j_new].is_snake_obstruction()\
                    or self.tiles[i_new][j_new].is_snake_obstruction()):
                    return "valid"
        return "non_SCC"
    
    def check_map_valid(self) -> str:
        SCC_count = 0
        visited = ([False]*self.columns)*self.rows
        for i in range(self.rows):
            for j in range(self.columns):
                if not visited[i][j]\
                and not self.tiles[i][j].is_snake_obstruction():
                    SCC_count += 1
                    result = self._dfs_check(i, j, visited)
                    if result != "valid":
                        return result
        if SCC_count < 0:
            return "no_space"
        if SCC_count > 1:
            return "multiple_SCC"
        return "valid"

