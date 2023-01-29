import pygame

pygame.init()
size = (350, 400)
screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 180, 200), (250, 250), 75)
    pygame.display.flip()

pygame.quit()
