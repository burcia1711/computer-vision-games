import pygame

#Initialize pygame
pygame.init()

#Creating a game window
WIDTH,HEIGHT=500,500
window=pygame.display.set_mode((WIDTH,HEIGHT))

#Colors
GREEN=(0,255,0)
MIXED=(15,55,150)
#Adding Font
font_name=pygame.font.SysFont("arial",32)
text=font_name.render("Hello",True,(255,0,0),GREEN)
text_coordinate=text.get_rect()
text_coordinate.center=(150,250)

# Adding external font
external_font=pygame.font.Font("Anton-Regular.ttf",64)
text2=external_font.render("Hello",True,(0,0,255),MIXED)
text2_coordinate=text2.get_rect()
text2_coordinate.center=(250,390)

working=True
while working:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            working=False

    window.blit(text,text_coordinate)
    window.blit(text2,text2_coordinate)
    pygame.display.update()



pygame.quit()