import pygame

#Initialize pygame
pygame.init()

# Creating game window
WIDTH, HEIGHT = 500, 550
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Load an image
drFrankenstein = pygame.image.load("frankenstein.png")
dr_coordinate = drFrankenstein.get_rect()
dr_coordinate.center = (150, 250)

working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
    window.blit(drFrankenstein, dr_coordinate)
    pygame.display.update()

pygame.quit()
