import os
import random
import time

import pygame

from window import HEIGHT, WIDTH, WIN


def path(name) -> str:
    return os.path.join(f"assets", name)


_boat_size = int(WIDTH // 5), int(WIDTH // 10)

BACKGROUND = pygame.image.load(path("waves.svg"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

BOAT_1 = pygame.image.load(path("boat-1.svg"))
BOAT_2 = pygame.image.load(path("boat-2.svg"))
BOAT_1 = pygame.transform.scale(BOAT_1, _boat_size)
BOAT_2 = pygame.transform.scale(BOAT_2, _boat_size)

TORPEDO = pygame.image.load(path("torpedo.svg"))
TORPEDO = pygame.transform.scale(TORPEDO, (int(_boat_size[0] // 2), int(_boat_size[1] // 2 * (TORPEDO.get_width() / TORPEDO.get_height()))))

MINE = pygame.image.load(path("mine.svg"))
MINE = pygame.transform.scale(MINE, (_boat_size[0] * 0.75, _boat_size[0] * 0.75))


def draw_background():
    WIN.blit(BACKGROUND, (0, 0))


def draw_window(boat: pygame.Rect):
    if int(time.time() * 4) % 4 in [1, 3]:
        WIN.blit(BOAT_1, (boat.x, boat.y))
    else:
        WIN.blit(BOAT_2, (boat.x, boat.y))


def draw_torpedoes(torpedoes: list[pygame.Rect]):
    for torpedo in torpedoes:
        WIN.blit(TORPEDO, (torpedo.x, torpedo.y))


def draw_mines(mines: list[pygame.Rect]):
    for mine in mines:
        WIN.blit(MINE, (mine.x, mine.y))


def new_mine() -> pygame.Rect:
    return pygame.Rect(int(WIDTH * 0.9), random.randint(0, int(HEIGHT // 2)), MINE.get_width(), MINE.get_height())
