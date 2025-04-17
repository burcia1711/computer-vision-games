import pygame

# Initialize pygame
pygame.init()

# Creating game window
WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Adding an image
monster = pygame.image.load("monster.png")
monster_coordinate = monster.get_rect()
monster_coordinate.center = (250, 350)

# Setting FPS
FPS = 30
clock = pygame.time.Clock()

# Creating game loop
working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and monster_coordinate.left > 0:
        monster_coordinate.x -= 5
    elif key[pygame.K_RIGHT] and monster_coordinate.right < 600:
        monster_coordinate.x += 5
    elif key[pygame.K_UP] and monster_coordinate.top > 0:
        monster_coordinate.y -= 5
    elif key[pygame.K_DOWN] and monster_coordinate.bottom < 600:
        monster_coordinate.y += 5
    window.fill((0, 0, 0))
    window.blit(monster, monster_coordinate)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()