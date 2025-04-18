import cv2
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Webcam Settings
webcam = cv2.VideoCapture(1)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Creating Game Window
WIDTH, HEIGHT = 1280, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

# FPS Value
FPS = 30
clock = pygame.time.Clock()

# Creating Game Loop
working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

    control, frame = webcam.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = np.rot90(rgb)
    background = pygame.surfarray.make_surface(rgb).convert()
    window.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
