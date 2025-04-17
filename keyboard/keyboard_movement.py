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

# Creating a game loop
working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_coordinate.y -= 5
            elif event.key == pygame.K_DOWN:
                player_coordinate.y += 5
            elif event.key == pygame.K_LEFT:
                player_coordinate.x -= 5
            elif event.key == pygame.K_RIGHT:
                player_coordinate.x += 5

    window.fill((0, 0, 0))
    window.blit(player, player_coordinate)
    pygame.display.update()

pygame.quit()
