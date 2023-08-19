from os import path, getcwd
from src.game_objects.map import Map
from src.game_objects.game_tiles import Grass, Wall
class MapHandler():
    """
    Map Handler class for the map.
    Can:
    create default map;
    save map to files;
    load map to files;
    read maps from strings;
    """
    def __init__(self) -> None:
        """
        Initialises the map Handler.
        Creates a default map for the snake.
        """
        self.read_map("")
        self.name = "default"

    def read_map(self, file_path: str = "") -> bool:
        """
        Reads the map from the given file path.
        If not given  any, creates the default map.
        Returns true when a map was sucessfuly created and false otherwise
        """
        if file_path == "":
            self.create_default_map(10, 10)
            return True

        elif path.exists(file_path) and path.isfile(file_path):
            return self._read_map_from_file(file_path)

        return False

    def create_default_map(self, rows: int, columns: int) -> None:
        """
        Changes the map into the default layot of only walls on
        the outer edge of the map and only grass in.
        """
        self.map = Map(rows, columns)
        for i in range(rows):
            for j in range(columns):
                if i == 0 or j == 0 or j==columns-1 or i==rows-1:
                    self.map.change_tile(i, j, Wall())
                else:
                    self.map.change_tile(i, j, Grass())

    def _read_map_from_file(self, file_path: str) -> bool:
        """
        Reads and creates map from the information on the given file path.
        Should only be used with existing file paths.
        Returns true if the map created is valid, false otherwise.
        """
        file = open(file_path, "r")
        map_lines = file.readlines()
        while len(map_lines) > 1\
              and map_lines[len(map_lines)-1] == "":
            map_lines.pop()

        return self.create_map_from_string_lines(map_lines)


