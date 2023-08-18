from unittest import TestCase
from src.game_objects.game_tiles import Grass, Wall
from src.game_objects.map import Map

def set_map_walls(map: Map) -> None:
    map.tiles = [[Wall()]*map.columns for i in range(map.rows)]

class TestingTile(TestCase):

    def test_no_space_map(self):
        map = Map(3,3)
        set_map_walls(map)
        self.assertEqual(map.check_map_valid(), "no_space")

        map = Map(1,1)
        set_map_walls(map)
        self.assertEqual(map.check_map_valid(), "no_space")

    def test_not_SCC_map(self):
        map = Map(3,3)
        set_map_walls(map)
        map[1][1] = Grass()
        self.assertEqual(map.check_map_valid(), "not_SCC")

        map = Map(5,5)
        set_map_walls(map)
        map[1][1] = Grass()
        self.assertEqual(map.check_map_valid(), "not_SCC")

        map[1][2] = Grass()
        map[2][2] = Grass()
        self.assertEqual(map.check_map_valid(), "not_SCC")
    
    def test_SCC_map(self):
        map = Map(5,5)
        set_map_walls(map)
        map[1][1] = Grass()
        map[1][2] = Grass()
        map[2][2] = Grass()
        map[2][1] = Grass()
        #print([[map[i][j].is_snake_obstruction() for j in range(map.columns)] for i in range(map.rows)])
        self.assertEqual(map.check_map_valid(), "valid")

    def test_out_of_bounds_map(self):
        map = Map(3,3)
        set_map_walls(map)
        map[0][0] = Grass()
        map[0][1] = Grass()
        map[1][0] = Grass()
        map[1][1] = Grass()
        self.assertEqual(map.check_map_valid(), "out_of_bounds")

        set_map_walls(map)
        map[2][2] = Grass()
        map[2][1] = Grass()
        map[1][2] = Grass()
        map[1][1] = Grass()
        self.assertEqual(map.check_map_valid(), "out_of_bounds")
