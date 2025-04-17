import pygame

#Initialize pygame
pygame.init()

#Creating game window
WIDTH,HEIGHT=1280,720
game_window=pygame.display.set_mode((WIDTH,HEIGHT))

background=pygame.image.load("background.jpg")
working=True
while working:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            working=False
    game_window.blit(background,(0,0))
    pygame.display.update()

pygame.quit()