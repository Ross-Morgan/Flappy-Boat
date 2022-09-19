import pygame
import pygame.mixer


def play_forever():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/wolfpack-8bit.mp3")
    pygame.mixer.music.play(loops=-1)
