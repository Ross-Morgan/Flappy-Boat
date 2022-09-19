import pygame

import game_loop


def main():
    pygame.display.set_icon(pygame.image.load("assets/window-icon.png"))
    pygame.display.set_caption("Flappy Boat")
    pygame.display.flip()

    game_loop.run_event_loop()


if __name__ == "__main__":
    main()
