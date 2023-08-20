from unittest import TestCase
from os import path
from src.game_objects.game_tiles import Grass, Wall
from src.game_objects.map_handler import MapHandler, SAVE_PATH

class TestingMapHandler(TestCase):

    def test_map_handler_conversion_from_string(self):
        map_handler = MapHandler()
        result = map_handler.convert_strings_to_map(["WWW", "WGW", "WWW"])

        self.assertEqual(map_handler.map.rows, 3)
        self.assertEqual(map_handler.map.columns, 3)
        self.assertTrue(isinstance(map_handler.map[0][0], Wall))
        self.assertTrue(isinstance(map_handler.map[1][0], Wall))
        self.assertTrue(isinstance(map_handler.map[2][0], Wall))
        self.assertTrue(isinstance(map_handler.map[1][1], Grass))
        self.assertTrue(isinstance(map_handler.map[2][2], Wall))
        self.assertFalse(result)
        self.assertEqual(map_handler.map.check_map_valid(), "not_SCC")

        result = map_handler.convert_strings_to_map(["WWWW", "WGGW", "WGGW", "WWWW"])
        self.assertTrue(result)
        self.assertEqual(map_handler.map.check_map_valid(), "valid")

    def test_map_handler_conversion_from_map(self):
        map_handler = MapHandler()

        result = map_handler.convert_strings_to_map(["WWWW", "WGGW", "WGGW", "WWWW"])

        self.assertEqual(map_handler.convert_map_into_strings(), ["WWWW", "WGGW", "WGGW", "WWWW"])

    def test_default_map_creator(self):
        map_handler = MapHandler()
        result = map_handler.create_default_map(3, 3)

        self.assertFalse(result)

        result = map_handler.create_default_map(5, 5)

        self.assertTrue(result)
        self.assertTrue(isinstance(map_handler.map[0][0], Wall))
        self.assertTrue(isinstance(map_handler.map[1][0], Wall))
        self.assertTrue(isinstance(map_handler.map[1][1], Grass))
        self.assertTrue(isinstance(map_handler.map[2][2], Grass))
        self.assertTrue(isinstance(map_handler.map[3][2], Grass))

        self.assertEqual(map_handler.convert_map_into_strings(), ["WWWWW", "WGGGW", "WGGGW", "WGGGW", "WWWWW"])

    def test_default_map_create_save_in_file(self):
        map_handler = MapHandler()
        map_handler.create_default_map(5, 5)
        map_handler.name = "test_default"
        result = map_handler.save_map()
        file_path = path.join(SAVE_PATH,  map_handler.name + ".txt")

        self.assertTrue(result)
        self.assertTrue(path.exists(file_path))
        self.assertTrue(path.isfile(file_path))

    def test_default_map_writing_save_in_file(self):
        map_handler = MapHandler()
        map_handler.create_default_map(5, 5)
        map_handler.name = "test_default"
        map_handler.save_map()
        file_path = path.join(SAVE_PATH,  map_handler.name + ".txt")

        file = open(file_path, "r")
        file_content = file.readlines()
        self.assertEqual(file_content, ["WWWWW\n", "WGGGW\n", "WGGGW\n", "WGGGW\n", "WWWWW\n"])
        file.close()
