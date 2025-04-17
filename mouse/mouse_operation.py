import pygame

# Initialize pygame
pygame.init()

# Creating game window
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Creating game loop
working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_value = event.pos[0]
            mouse_y_value = event.pos[1]
            print("X axis:", mouse_x_value, " ", "Y axis:", mouse_y_value)

pygame.quit()
