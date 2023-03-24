import sys
import pygame
from pathDrawHandler import PathDrawHandler

pygame.init()

pygame.key.set_repeat()

size = width, height = 750, 750
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# grid = Grid(50, 10)
pathHandler = PathDrawHandler(75, 10)

frames = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    delay = pathHandler.update()
    screen.fill(black)
    pathHandler.render(screen)

    pygame.display.flip()
    frames.tick(60)
    if (delay):
        pygame.time.delay(100)
