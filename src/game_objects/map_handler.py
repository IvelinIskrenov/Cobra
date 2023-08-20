from os import path, getcwd
from src.game_objects.map import Map
from src.game_objects.game_tiles import Grass, Wall

SAVE_PATH = path.join(getcwd(), "src", "maps")

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
        Creates a default map for the cobra.
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
            return self.create_default_map(10, 10)

        elif path.exists(file_path) and path.isfile(file_path):
            return self._read_map_from_file(file_path)

        return False

    def create_default_map(self, rows: int, columns: int) -> bool:
        """
        Changes the map into the default layot of only walls on
        the outer edge of the map and only grass in.
        Returns true if map is successfully created, false otherwise.
        """
        self.map = Map(rows, columns)
        for i in range(rows):
            for j in range(columns):
                if i == 0 or j == 0 or j==columns-1 or i==rows-1:
                    self.map.change_tile(i, j, Wall())
                else:
                    self.map.change_tile(i, j, Grass())

        result = (self.map.check_map_valid() == "valid")
        return result

    def _read_map_from_file(self, file_path: str) -> bool:
        """
        Reads and creates map from the information on the given file path.
        Should only be used with existing file paths.
        Returns true if the map created is valid, false otherwise.
        """
        file = open(file_path, "r")
        map_lines = file.readlines()
        while len(map_lines) > 1 and map_lines[len(map_lines)-1] == "":
            map_lines.pop()
        file.close()

        return self.convert_strings_to_map(map_lines)

    def convert_strings_to_map(self,  map_lines: list[str]) -> bool:
        """
        Creates map from the given lines of string.
        Returns false if the map is impossible to create
        and true otherwise.
        """
        if len(map_lines) == 0:
            return False

        for line in map_lines:
            if line[-1] == "\n":
                line[:-1] #remove new line

        self.map = Map(len(map_lines), len(map_lines[0]))

        for i, line in enumerate(map_lines):
            if len(line) != len(map_lines[0]):
                return False
            for j, el in enumerate(line):
                if not self._set_str_to_tile(i, j, el):
                    return False

        if self.map.check_map_valid() != "valid":
            return False
        return True


    def _set_str_to_tile(self, i: int, j: int, element: str) -> bool:
        """
        Changes the i-th and j-th tile to the given str:
        'W' for wall;
        'G' for grass;
        Returns false if the str is invalid. True otherwise."""
        if element == "W":
            self.map.change_tile(i, j, Wall())
        elif element == "G":
            self.map.change_tile(i, j, Grass())
        else:
            return False
        return True

    def save_map(self) -> bool:
        """
        Saves the map in a file with the current map name in src/maps
        if the map is valid. Returns true if successfull,
        false otherwise.
        """
        save_file_path = path.join(SAVE_PATH, self.name + ".txt")
        if self.map.check_map_valid() != "valid":
            return False
        self._write_map_on_file(save_file_path)
        return True


    def _write_map_on_file(self, file_name: str) -> None:
        """
        Writes information about the map on the given file path.
        """
        file = open(file_name, "w")
        result = self.convert_map_into_strings()
        for line in result:
            file.write(line)
            file.write("\n")
        file.close()

    def convert_map_into_strings(self) -> list[str]:
        """Converts the map into a string"""
        result = []
        for i in range(self.map.rows):
            line = ""
            for j in range(self.map.columns):
                line += self._get_tile_representation(i, j)
            result.append(line)
        return result

    def _get_tile_representation(self, i: int, j: int) -> str:
        """
        Returns the string representation of the tile.
        """
        return self.map[i][j].tile_to_str()
        return "?"
