import pygame
from pygame import mixer
#initializing
pygame.init()
pygame.display.set_caption("Nishimukai: Insurrection of Verrücktpixelnacht")
# icon = pygame.image.load('joystick.png').convert_alpha()
# pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

#background music
mixer.music.load('title_screen.wav')
mixer.music.play(-1)

#title screeen elements
background = pygame.image.load('media/titlebackground.jpg').convert_alpha()


running = True
selection = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selection = 1


    screen.blit(background, (0,0))

    #selection
    if selection == 1:
        import version1

    clock.tick(60)
    pygame.display.update()
