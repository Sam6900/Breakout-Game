import pygame
from sys import exit


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/paddle.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(width/2, height))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += 4
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 4

    def update(self):
        self.player_input()


class Tile(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.image.load(f"assets/tiles/{color}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 0))


pygame.init()
win_size = width, height = 448, 550
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

paddle = pygame.sprite.GroupSingle()
paddle.add(Paddle())

tiles_group = pygame.sprite.Group()
tiles_group.add(Tile("blue"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("#562B08")
    paddle.draw(screen)
    paddle.update()
    tiles_group.draw(screen)

    pygame.display.update()
    clock.tick(60)
