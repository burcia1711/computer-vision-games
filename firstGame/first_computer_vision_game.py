import pygame
import mediapipe as mp
import cv2
import numpy as np
import random

# Setting up Webcam
webcam = cv2.VideoCapture(1)
webcam.set(3, 1280)
webcam.set(4, 720)

# Initialize Pygame
pygame.init()

# Creating Game Window
WIDTH, HEIGHT = 1280, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Background Music and Sound Effects
pygame.mixer.music.load("cvgamesound.wav")
pygame.mixer.music.play(-1, 0.0)
destroying_virus = pygame.mixer.Sound("collect.wav")

# Adding main Character and Virus
player = pygame.image.load("avatar.png")
player_coordinate = player.get_rect()

candle = pygame.image.load("candle.png")
candle_coordinate = candle.get_rect()
candle_coordinate.center = (250, 250)

# Colours
burgundy = (142, 22, 22)
cream = (248, 238, 223)

# Font
FONT = pygame.font.Font("Anton-Regular.ttf", 64)

# Hand Model
hand_model = mp.solutions.hands

# Score
SCORE = 0

# Game Loop
working = True
with hand_model.Hands(min_tracking_confidence=0.5, min_detection_confidence=0.5) as hand:
    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
        # OpenCV Operation
        control, frame = webcam.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(rgb)
        if result.multi_hand_landmarks:
            for handLandmark in result.multi_hand_landmarks:
                index_finger_coordinate = handLandmark.landmark[8]
                x = int(index_finger_coordinate.x * WIDTH)
                y = int(index_finger_coordinate.y * HEIGHT)
                player_coordinate.center = (x, y)
        rgb = np.rot90(rgb)
        background = pygame.surfarray.make_surface(rgb).convert()
        background = pygame.transform.flip(background, True, False)
        window.blit(background, (0, 0))
        window.blit(player, player_coordinate)
        window.blit(candle, candle_coordinate)
        TEXT = FONT.render("Score: " + str(SCORE), True, cream, burgundy)
        TEXT_COORDINATE = TEXT.get_rect()
        TEXT_COORDINATE.center = (640, 60)
        window.blit(TEXT, TEXT_COORDINATE)
        pygame.draw.line(window, (0, 0, 0), (0, 121), (1280, 121), 5)
        if player_coordinate.colliderect(candle_coordinate):
            destroying_virus.play()
            candle_coordinate.x = random.randint(0, 1000)
            candle_coordinate.y = random.randint(130, 500)
            SCORE += 1
        pygame.display.update()

pygame.quit()
