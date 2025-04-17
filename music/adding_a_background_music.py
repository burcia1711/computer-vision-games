import pygame

# Initialize pygame
pygame.init()

# Creating a game window
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.mixer.music.load("background_music.wav")
pygame.mixer.music.play(-1)

# Creating a game loop
working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

pygame.quit()
