import pygame


WIDTH, HEIGHT = 1280, 720
CENTRE_ADJ = int(HEIGHT // 10)
BORDER = pygame.Rect(0, int(HEIGHT * 0.15), WIDTH, int(HEIGHT * 0.7))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
