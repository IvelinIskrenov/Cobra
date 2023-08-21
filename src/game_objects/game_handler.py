import asyncio
import pygame
import sys
from pygame import image
from pygame.locals import *
from random import randint
from os import path, getcwd
from src.game_objects.map_handler import MapHandler
from src.game_objects.cobra import Cobra
from src.game_objects.game_tiles import Grass, Wall
from src.base.tile import Tile

SAVE_PATH = path.join(getcwd(), "src", "maps")

APPLE_SPRITE = image.load(path.join(getcwd(), "src", "sprites", "baby.png"))

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
        self.map_handler.create_default_map(10, 10)
        self.cobra = Cobra()
        self.apple: Tile = Tile(0, 0, APPLE_SPRITE)
        self._create_new_apple()
        self.screen = pygame.display.set_mode((1400, 700), pygame.RESIZABLE)
        self.keys_pressed =\
            {
            "player_movement": [False, False, False, False],
            }
        self.next_step_time = 4000 # ms

    def _create_new_apple(self):
        """Creates new apple on the map on a random spot"""
        while True:
            i = randint(0, self.map_handler.map.rows - 1)
            j = randint(0, self.map_handler.map.columns - 1)

            if self.map_handler.map[i][j].is_cobra_obstruction():
                continue
            for part in self.cobra.parts:
                if i == part.x and j == part.y:
                    continue
            break
        self.apple.set_coordinates(i,
                                   j,
                                   self.map_handler.map.position.x,
                                   self.map_handler.map.position.y)

    def get_key_presses(self):
        """
        Gets the key presses from the user and evaluates the events.
        """
        for event in pygame.event.get():
            #Existing game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            #Changing window size
            #elif event.type == VIDEORESIZE:
            #    Game.resizable_screen =\
            #        pygame.display.set_mode((event.size[0],event.size[0]/2),
            #                                RESIZABLE)
            #    self.screen_scaling = event.size[0]/WINDOW_SIZE[0]


            elif event.type == pygame.KEYDOWN:

                #Player movement
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.keys_pressed["player_movement"][0] = True
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.keys_pressed["player_movement"][1] = True
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.keys_pressed["player_movement"][2] = True
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.keys_pressed["player_movement"][3] = True

    def evaluate_key_presses(self):
        """
        Evaluates events based on pressed keys from user.
        """
        for direction in range(4):
            if self.keys_pressed["player_movement"][direction]:
                self.cobra.switch_direction_to_input(direction + 1)
                self.keys_pressed["player_movement"][direction] = False

    def cobra_hit_something(self):
        head = self.cobra.head
        if self.map_handler.map[head.x][head.y].is_cobra_obstruction():
            return True
        for part in self.cobra.parts:
            if head.x == part.x and head.y == part.y:
                return True
        return False

    def render(self) -> None:
        """Renders all the needed objects to the screen"""
        self.screen.fill((0,0,0))
        self.map_handler.render(self.screen)
        self.cobra.render(self.screen)
        self.apple.render(self.screen)

    def handle_movement(self) -> None:
        time = self.clock.get_time()
        self.next_step_time -= time

        if self.next_step_time <= 0:
            self.next_step_time = 500
            if self.cobra_hit_something():
                self.cobra.deactivate()
            self.cobra.next_step()

        if self.cobra.head.x == self.apple.x\
            and self.cobra.head.y == self.apple.y:
            self.cobra.eaten = True
            self._create_new_apple()

    def _update(self):
        """Updates the game windows to the next frame"""
        self.get_key_presses()
        self.evaluate_key_presses()
        self.handle_movement()
        self.render()
        pygame.display.flip()

    async def start(self):
        """
        Starts the game.
        """
        self.game_state = "SnakeGame"
        self.clock.tick(120) # to refresh the clock rate
        while True:
            self._update()
            await asyncio.sleep(0)
            self.clock.tick(120)