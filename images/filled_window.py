import pygame

#Initialize pygame
pygame.init()

# Creating a window
WIDTH=450
HEIGHT=600
window=pygame.display.set_mode((WIDTH,HEIGHT))
WHITE=(255,255,255)
BLUE=(0,0,255)
pygame.draw.circle(window,WHITE,(75,75),75,-2)
pygame.draw.rect(window,(255,0,0),(89,250,250,155),-8)
working=True
while working:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            working=False
    window.fill(BLUE)
    pygame.display.update()




pygame.quit()