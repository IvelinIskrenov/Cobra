import unittest
import sys
import os
sys.path.append(os.getcwd())
from src.tests.tile_test import *
from src.tests.game_tiles_test import *
from src.tests.map_tests import *
from src.tests.map_handler_test import *
from src.tests.cobra_part_test import *

if __name__ == '__main__':
    unittest.main()