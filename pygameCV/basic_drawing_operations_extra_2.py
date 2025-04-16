import pygame

#Initialize pygame
pygame.init()

WIDTH=750
HEIGHT=500
surface_area=pygame.display.set_mode((WIDTH,HEIGHT))
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
DARK_BLUE=(7,7,165)
BROWN=(135,90,0)
pygame.draw.line(surface_area,DARK_BLUE,(0,0),(500,400),3)
pygame.draw.line(surface_area,BROWN,(10,25),(100,366),7)
pygame.draw.line(surface_area,(135,0,0),(50,50),(175,298),4)
working=True
while working:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            working=False

    #Updating display / window
    pygame.display.update()

pygame.quit()