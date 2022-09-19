import pygame

import game_loop
import music


def main():
    pygame.display.set_caption("Flappy Boat")
    pygame.display.flip()

    music.play_forever()
    game_loop.run_event_loop()


if __name__ == "__main__":
    main()
