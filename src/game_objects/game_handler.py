import asyncio
import pygame
from random import randint
from os import path, getcwd
from src.game_objects.map_handler import MapHandler
from src.game_objects.game_tiles import Grass, Wall

SAVE_PATH = path.join(getcwd(), "src", "maps")

class GameHandler():
    """
    GameHandler for the level editor and the game.
    """
    def __init__(self) -> None:
        """
        Initialises the map Handler.
        Creates a default map for the cobra.
        """
        self.clock = pygame.time.Clock()
        self.map_handler = MapHandler()
        self.map_handler.create_default_map(8, 8)
        self._create_new_apple()
        self.screen = pygame.display.set_mode((1400, 700), pygame.RESIZABLE)

    def _create_new_apple(self):
        """Creates new apple on the map on a random spot"""
        while True:
            i = randint(0, self.map_handler.map.rows - 1)
            j = randint(0, self.map_handler.map.columns - 1)

            if not self.map_handler.map[i][j].is_cobra_obstruction():
                break
        self.apple_coordinate_x = i
        self.apple_coordinate_y = j

    def render(self) -> None:
        """Renders all the needed objects to the screen"""
        self.screen.fill((0,0,0))
        self.map_handler.render(self.screen)

    def _update(self):
        """Updates the game windows to the next frame"""
        self.render()
        pygame.display.flip()

    async def start(self):
        """
        Starts the game.
        """
        self.game_state = "SnakeGame"
        while True:
            self._update()
            await asyncio.sleep(0)
            self.clock.tick(120)