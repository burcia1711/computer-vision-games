import pygame

# Initialize pygame
pygame.init()

# Creating game window
WIDTH, HEIGHT = 500, 550
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Load an image
dr = pygame.image.load("frankenstein.png")
dr_coordinate = dr.get_rect()
dr_coordinate.center = (200, 250)

monster = pygame.image.load("monster.png")
monster_coordinate = monster.get_rect()
monster_coordinate.center = (300, 250)

working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
    window.blit(monster, monster_coordinate)
    window.blit(dr, dr_coordinate)

    pygame.display.update()

pygame.quit()
