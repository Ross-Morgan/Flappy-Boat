import time

import pygame

import movement
import sprites
from sprites import BOAT_1, TORPEDO
from window import HEIGHT, WIDTH

FPS = 60
TORPEDO_DELAY = 0.5
MINE_DELAY = 1

def run_event_loop():
    clock = pygame.time.Clock()
    running = True

    mines = []
    torpedoes = []

    last_mine_created = 0
    last_time_fired = 0

    boat = pygame.Rect(int(WIDTH // 15), int((HEIGHT // 2) - (BOAT_1.get_height() // 2)), BOAT_1.get_height(), BOAT_1.get_width())

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                boat.x = -1000
                boat.y = -1000

                mines.clear()
                torpedoes.clear()

                running = False

            if pygame.key.get_pressed()[pygame.K_SPACE] and time.time() > last_time_fired + TORPEDO_DELAY:
                torpedo = pygame.Rect(boat.x + boat.width, boat.y + int(boat.height // 4), TORPEDO.get_width(), TORPEDO.get_height())
                torpedoes.append(torpedo)

                last_time_fired = time.time()

        if last_mine_created + MINE_DELAY < time.time():
            mines.append(sprites.new_mine())

            last_mine_created = time.time()

        sprites.draw_background()

        keys_pressed = pygame.key.get_pressed()

        movement.handle_boat_movement(keys_pressed, boat)
        movement.handle_torpedo_movement(torpedoes)
        movement.handle_mine_movement(mines, torpedoes, boat)

        sprites.draw_torpedoes(torpedoes)
        sprites.draw_mines(mines)
        sprites.draw_window(boat)

        pygame.display.update()

    pygame.quit()
