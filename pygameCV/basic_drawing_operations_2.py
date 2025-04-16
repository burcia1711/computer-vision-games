import pygame

#Initialize pygame
pygame.init()

# Creating a window
WIDTH=450
HEIGHT=600
window=pygame.display.set_mode((WIDTH,HEIGHT))
WHITE=(255,255,255)
pygame.draw.circle(window,WHITE,(75,75),75,3)
pygame.draw.rect(window,(255,0,0),(89,250,100,50),6)
working=True
while working:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            working=False

    pygame.display.update()




pygame.quit()