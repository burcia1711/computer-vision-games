import pygame

#Initialize pygame
pygame.init()

#Creating a game window
WIDTH,HEIGHT=500,500
window=pygame.display.set_mode((WIDTH,HEIGHT))

#Adding Font
font_name=pygame.font.SysFont("arial",32)
text=font_name.render("Hello",True,(255,0,0))
text_coordinate=text.get_rect()
text_coordinate.center=(150,250)

working=True
while working:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            working=False

    window.blit(text,text_coordinate)
    pygame.display.update()



pygame.quit()