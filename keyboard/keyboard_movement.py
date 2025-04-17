import pygame

# Initialize pygame
pygame.init()

# Creating a game window
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))


# Defining a character
player = pygame.image.load("avatar.png")
player_coordinate = player.get_rect()
player_coordinate.center = (250, 275)

# Setting FPS
FPS = 30
clock = pygame.time.Clock()

# Creating a game loop
working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player_coordinate.x-=5
    elif key[pygame.K_RIGHT]:
        player_coordinate.x+=5
    elif key[pygame.K_UP]:
        player_coordinate.y-=5
    elif key[pygame.K_DOWN]:
        player_coordinate.y+=5

    window.fill((0, 0, 0))
    window.blit(player, player_coordinate)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
