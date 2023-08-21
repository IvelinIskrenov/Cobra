import asyncio
import pygame
import sys
from pygame import image, Surface
from pygame.locals import *
from random import randint
from os import path, getcwd
from src.game_objects.map_handler import MapHandler
from src.game_objects.cobra import Cobra
from src.game_objects.game_tiles import Grass, Wall
from src.base.tile import Tile

SAVE_PATH = path.join(getcwd(), "src", "maps")

APPLE_SPRITE = image.load(path.join(getcwd(), "src", "sprites", "baby.png"))

pointer = Tile(0, 0, Surface((10, 10)), 10, 10)

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
        self.map_handler.read_map(path.join(getcwd(), "src", "maps", "default.txt"))
        self.cobra = Cobra()
        self.apple: Tile = Tile(0, 0, APPLE_SPRITE)
        self._create_new_apple()
        self.screen = pygame.display.set_mode((1400, 700), pygame.RESIZABLE)
        self.reset_keys()
        self.next_step_time = 4000 # ms
        self.state = "game"

    def _create_new_apple(self) -> None:
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

    def get_key_presses(self) -> None:
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
                if  event.key == ord('p'):
                    self.keys_pressed["switch"] = True
                if event.key == ord('l'):
                    self.keys_pressed["inc_columns"] = True
                if event.key == ord('k'):
                    self.keys_pressed["inc_rows"] = True
                if event.key == ord('j'):
                    self.keys_pressed["decr_rows"] = True
                if event.key == ord('h'):
                    self.keys_pressed["decr_columns"] = True
                if event.key == ord('g'):
                    self.keys_pressed["grass"] = True
                if event.key == ord('t'):
                    self.keys_pressed["wall"] = True

    def evaluate_key_presses_for_game(self) -> None:
        """
        Evaluates events based on pressed keys from user.
        """
        for direction in range(4):
            if self.keys_pressed["player_movement"][direction]:
                self.cobra.switch_direction_to_input(direction + 1)
        if self.keys_pressed["switch"]:
                self.state = "level_editor"
        self.reset_keys()

    def cobra_hit_something(self) -> bool:
        """
        Checks if the cobra hit itself or block tile
        Returns true if yes, false otherwise
        """
        head = self.cobra.head
        if self.map_handler.map[head.y][head.x].is_cobra_obstruction():
            return True
        for part in self.cobra.parts:
            if head.x == part.x and head.y == part.y:
                return True
        return False

    def render_game(self) -> None:
        """Renders all the needed objects to the screen"""
        self.screen.fill((0,0,0))
        self.map_handler.render(self.screen)
        self.cobra.render(self.screen)
        self.apple.render(self.screen)

    def handle_movement(self) -> None:
        """
        Handles the movement for the cobra.
        Checks for hits and if the cobra ate an apple.
        """
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

    def reset_keys(self) -> None:
        """Resets the keys to default value."""
        self.keys_pressed =\
            {
            "player_movement": [False, False, False, False],
            "switch" : False,
            "inc_columns" : False,
            "inc_rows" : False,
            "decr_rows" : False,
            "decr_columns" : False,
            "grass" : False,
            "wall" : False
            }

    def reset_game(self)-> None:
        """Starts the game again with the edited map if it is possible"""
        self.clock = pygame.time.Clock()
        if not self.map_handler.save_map():
            self.map_handler.create_default_map(
                max(self.map_handler.map.rows, 4),
                max(self.map_handler.map.columns, 4)
                )
        self.cobra = Cobra()
        self.apple: Tile = Tile(0, 0, APPLE_SPRITE)
        self._create_new_apple()
        self.reset_keys()
        self.next_step_time = 4000 # ms
        self.state = "game"

    def evaluate_key_presses_for_level_editor(self) -> None:
        """
        Checks which keys were pressed during the
        last frame and evaluates the command
        """
        if  self.keys_pressed["switch"]:
            self.reset_game()
            return
        if self.keys_pressed["inc_columns"]:
            self.map_handler.create_default_map(
                self.map_handler.map.rows, self.map_handler.map.columns + 1)
        if self.keys_pressed["inc_rows"]:
            self.map_handler.create_default_map(
                self.map_handler.map.rows + 1, self.map_handler.map.columns)
        if self.keys_pressed["decr_rows"]:
            self.map_handler.create_default_map(
                self.map_handler.map.rows - 1, self.map_handler.map.columns)
        if self.keys_pressed["decr_columns"]:
            self.map_handler.create_default_map(
                self.map_handler.map.rows, self.map_handler.map.columns - 1)
        if self.keys_pressed["wall"]:
            self.map_handler.map.change_tile(pointer.y, pointer.x, Wall())
        if self.keys_pressed["grass"]:
            self.map_handler.map.change_tile(pointer.y, pointer.x, Grass())

        if self.keys_pressed["player_movement"][0]: #left
            pointer.set_coordinates(
                abs((pointer.x - 1)),
                pointer.y
            )
        if self.keys_pressed["player_movement"][1]: #right
            pointer.set_coordinates(
                (pointer.x + 1) % self.map_handler.map.columns,
                pointer.y
            )
        if self.keys_pressed["player_movement"][2]: #up
            pointer.set_coordinates(
                pointer.x,
                abs(pointer.y - 1)
            )
        if self.keys_pressed["player_movement"][3]: #down
            pointer.set_coordinates(
                pointer.x,
                (pointer.y + 1) % self.map_handler.map.rows,
            )

        self.reset_keys()

    def render_level_editor(self) -> None:
        """Renders the things in the level editor on the screen foer the user."""
        self.map_handler.render(self.screen)
        pointer.render(self.screen)

    def _update(self) -> None:
        """Updates the game windows to the next frame"""
        self.get_key_presses()
        if self.state == "game":
            self.evaluate_key_presses_for_game()
            self.handle_movement()
            self.render_game()
        else:
            self.evaluate_key_presses_for_level_editor()
            self.render_level_editor()
        pygame.display.flip()

    async def start(self) -> None:
        """
        Starts the game.
        """
        self.game_state = "SnakeGame"
        self.clock.tick(120) # to refresh the clock rate
        while True:
            self._update()
            await asyncio.sleep(0)
            self.clock.tick(120)