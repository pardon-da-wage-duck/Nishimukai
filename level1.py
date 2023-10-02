import pygame

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

#title screeen elements
background = pygame.image.load('media/background.png').convert_alpha()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

    screen.blit(background, (0,0))

    #selection

    clock.tick(60)
    pygame.display.update()