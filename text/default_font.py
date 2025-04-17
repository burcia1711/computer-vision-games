import pygame

# Initialize pygame
pygame.init()

font_lists=pygame.font.get_fonts()

for font in font_lists:
    print(font)