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


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/ball.png")
        self.rect = self.image.get_rect(center=(width/2, height/2))
        self.speed_x = 3
        self.speed_y = 3

    def ball_movement(self):
        if self.rect.right >= width:
            self.speed_x = -3
        elif self.rect.left <= 0:
            self.speed_x = 0
        elif self.rect.top <= 0:
            self.speed_y = 3
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def update(self):
        self.ball_movement()


class Tile(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        super().__init__()
        self.image = pygame.image.load(f"assets/tiles/{color}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


pygame.init()
win_size = width, height = 448, 550
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

paddle = pygame.sprite.GroupSingle()
paddle.add(Paddle())

ball = pygame.sprite.GroupSingle()
ball.add(Ball())

tiles_group = pygame.sprite.Group()
tile_order = ["pink", "pink", "red", "red", "orange", "orange"]
tile_width, tile_height = 64, 32

for tile_index, tile_color in enumerate(tile_order):
    for i in range(0, int(width/tile_width)):
        tiles_group.add(Tile(tile_color, (i * tile_width, tile_index * tile_height)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")
    tiles_group.draw(screen)

    paddle.draw(screen)
    paddle.update()

    ball.draw(screen)
    ball.update()

    pygame.display.update()
    clock.tick(60)
