from unittest import TestCase
from pygame import Vector2
from src.game_objects.game_tiles import Grass, Wall
from src.game_objects.map import Map

def set_map_walls(map: Map) -> None:
    map.tiles = [[Wall()]*map.columns for i in range(map.rows)]

class TestingMapDFS(TestCase):

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

    def test_multiple_SCC(self):
        map = Map(6,6)
        set_map_walls(map)
        map[1][1] = Grass()
        map[1][2] = Grass()
        map[2][1] = Grass()
        map[2][2] = Grass()

        map[4][4] = Grass()
        map[3][4] = Grass()
        map[4][3] = Grass()
        map[3][3] = Grass()
        self.assertEqual(map.check_map_valid(), "multiple_SCC")


class TestingMapRendering(TestCase):
    def test_render_positions(self):
        map = Map(3, 3)
        width = map[1][1].position.x
        height = map[1][1].position.y
        self.assertEqual(map[0][0].position, Vector2(0, 0))
        self.assertEqual(map[1][1].position, Vector2(width, height))
        self.assertEqual(map[1][2].position, Vector2(2*width, height))
        self.assertEqual(map[2][1].position, Vector2(width, 2*height))

        map = Map(3, 3, Vector2(2, 3))
        self.assertEqual(map[0][0].position, Vector2(2, 3))
        self.assertEqual(map[1][1].position, Vector2(width + 2, height + 3))
        self.assertEqual(map[1][2].position, Vector2(2*width + 2, height + 3))
        self.assertEqual(map[2][1].position, Vector2(width + 2, 2*height + 3))

    def test_tile_switch(self):
        map = Map(2, 2)
        old_render_position = map[1][1].position
        map.change_tile(1, 1, Grass())
        self.assertEqual(old_render_position, map[1][1].position)

        map = Map(3, 3, Vector2(2, 3))
        old_render_position = map[2][2].position
        map.change_tile(2, 2, Grass())
        self.assertEqual(old_render_position, map[2][2].position)
