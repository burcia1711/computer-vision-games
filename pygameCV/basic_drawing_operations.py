import pygame

# initialise pygame
pygame.init()

WIDTH = 750
HEIGHT = 500
surface_area = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.draw.line(surface_area, GREEN, (0,0), (500,400),3)
pygame.draw.line(surface_area, RED, (10,25), (100,333),7)
working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

    # updating display / window
    pygame.display.update()


pygame.quit()
