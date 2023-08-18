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
        self.tiles: list[list[Tile]] = [[Tile()]*columns for i in range(rows)]

    def __getitem__(self, key) -> list[Tile]:
        """Override to [], for easier access."""
        return self.tiles[key]

    def _DFS_check( self,
                    i: int,
                    j: int,
                    visited: list[list[bool]]) -> str:
        """
        Given tile coordinates on the map:
        Checks if the map is valid with depth first search.
        Returns "valid" if yes.
        if no - returns:
        "not_SCC" if the component is not strongly connected,
        since the snake won't be able to go both ways;
        "out_of_bounds" if the snake can get out of the map.
        """
        if i<0 or i>=self.rows or j<0 or j>=self.columns:
            return "out_of_bounds"
        if visited[i][j]:
            return "valid"
        if self[i][j].is_snake_obstruction():
            visited[i][j] = True
            return "valid"
        visited[i][j] = True
        directions = [1, -1]

        for direction in directions:
            result = self._DFS_check(i + direction, j, visited)
            if result != "valid":
                return result
            result = self._DFS_check(i, j + direction, visited)
            if result != "valid":
                return result

        for direction_x in directions:
            for direction_y in directions:
                i_new = i + direction_x
                j_new = j + direction_y
                if not\
                    (self[i_new][j_new].is_snake_obstruction()\
                    or self[i][j_new].is_snake_obstruction()\
                    or self[i_new][j_new].is_snake_obstruction()):
                    return "valid"
        return "not_SCC"
    
    def check_map_valid(self) -> str:
        """
        Checks if the map is valid.
        Returns "valid" if yes.
        if no - returns:
        "not_SCC" if the component is not strongly connected,
        since the snake won't be able to go both ways;
        "multiple_SCC" if the SCC's are more than 1,
        since the snake cannot travel between them;
        "no_space" if there is no tile for the snake;
        "out_of_bounds" if the snake can get out of the map.
        """
        SCC_count = 0
        visited = [[False]*self.columns]*self.rows
        for i in range(self.rows):
            for j in range(self.columns):
                if not visited[i][j]\
                and not self[i][j].is_snake_obstruction():
                    SCC_count += 1
                    result = self._DFS_check(i, j, visited)
                    if result != "valid":
                        return result
        if SCC_count == 0:
            return "no_space"
        if SCC_count > 1:
            return "multiple_SCC"
        return "valid"

