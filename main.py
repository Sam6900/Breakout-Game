import pygame
from sys import exit

pygame.init()
win_size = width, height = 400, 600
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Breakout Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
