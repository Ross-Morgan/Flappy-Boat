import pygame

from events import GAME_OVER
from window import HEIGHT, BORDER, CENTRE_ADJ

BOAT_VELOCITY = 3
TORPEDO_VELOCITY = 10
MINE_VELOCITY_X = 5
MINE_VELOCITY_Y = 1

def vcentre(sprite: pygame.Rect):
    return sprite.y + int(sprite.height // 2)


def handle_boat_movement(keys_pressed: list[bool], boat: pygame.Surface):
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and vcentre(boat) - CENTRE_ADJ - BOAT_VELOCITY > BORDER.top:  # Up arrow or w
        boat.y -= BOAT_VELOCITY
    if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and vcentre(boat) + BOAT_VELOCITY < BORDER.bottom:  # Down arrow or s
        boat.y += BOAT_VELOCITY


def handle_torpedo_movement(torpedoes: list[pygame.Rect]):
    for torpedo in torpedoes:
        torpedo.x += TORPEDO_VELOCITY

        if not torpedo.colliderect(pygame.Rect(0, 0, *pygame.display.get_window_size())):
            torpedoes.remove(torpedo)


def handle_mine_movement(mines: list[pygame.Rect], torpedoes: list[pygame.Rect], boat: pygame.Rect):
    for mine in mines:
        for torpedo in torpedoes:
            if mine.colliderect(torpedo):
                mines.remove(mine)
                torpedoes.remove(torpedo)

    for mine in mines:
        if mine.y - mine.height > HEIGHT or mine.x + mine.width < 0:
            mines.remove(mine)

        closest_mine_x: tuple[int, int] = min(map(lambda t: (t[1].x, t[0]), enumerate(mines)))
        closest_mine = mines[closest_mine_x[1]]

        if closest_mine.colliderect(boat):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        mine.x -= MINE_VELOCITY_X
        mine.y += MINE_VELOCITY_Y

