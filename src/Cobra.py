import sys
import os
import pygame
import asyncio
sys.path.append(os.getcwd())
from src.game_objects.game_handler import GameHandler


pygame.init()

pygame_icon = pygame.image.load(os.path.join("src", "sprites", "Grass.png"))
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption('Cobra')


game = GameHandler()

asyncio.run(game.start())