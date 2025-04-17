import pygame

# initialize pygame
pygame.init()

WIDTH, HEIGHT = 700, 800
surface_window = pygame.display.set_mode((WIDTH, HEIGHT))

working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False


pygame.quit()