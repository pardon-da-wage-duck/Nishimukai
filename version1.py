# import the pygame module, so you can use it
import pygame
import random
from pygame import mixer

# initializing pygame
pygame.init()

# Setting Title and Icon
pygame.display.set_caption("Nishimukai: Insurrection of Verrücktpixelnacht")
# icon = pygame.image.load('joystick.png')
# pygame.display.set_icon(icon)

# Setting Window
screen = pygame.display.set_mode((1200, 800))

# setting time
clock = pygame.time.Clock()

#background music
mixer.music.load('xomu_last_dance.wav')
mixer.music.play(-1)

#sound effects
popcat_sound = mixer.Sound('popcat sound.wav')

# Background
background = pygame.image.load('media/background.png').convert_alpha()
cloud = pygame.image.load('media/cloud.png').convert_alpha()

# Player sprite
playerImgL = pygame.image.load('media/marisamini.png').convert_alpha()
playerImgR = pygame.image.load('media/marisamini_inverse.png').convert_alpha()
playerCircle = pygame.image.load('media/playercircle.png').convert_alpha()
playerX = 400
playerY = 600
direction = "left"
playeralive = True

# bongo cat sprite
bongocat_f1 = pygame.image.load('media/bongocat_f1.gif').convert_alpha()
bongocat_f2 = pygame.image.load('media/bongocat_f2.gif').convert_alpha()
bongoX = random.randint(0, 786)
bongoY = 85
bongoshift = 1
bongohealth = 100
bongoalive = True

# pop cat sprite
popcat_f1 = pygame.image.load('media/popcat_f1.gif').convert_alpha()
popcat_f2 = pygame.image.load('media/popcat_f2.gif').convert_alpha()
popcatXList = []
popcatYList = []
popcathealth = []
popcatkills = 0
for i in range(5):
    popcatXList.append(random.randint(0, 786))
    popcatYList.append(170)
    popcathealth.append(20)

# Player bullet
bulletp = pygame.image.load('media/bullet_player.png').convert_alpha()
bulletp_XList = []
bulletp_YList = []
for i in range(40):
    bulletp_XList.append(playerX)
    bulletp_YList.append(playerY)

# Cat bullet
bulletc = pygame.image.load('media/bullet_cat.png').convert_alpha()
bulletcX = []
bulletcY = []
bulletdirect = []
for i in range(5):
    for i in range(len(popcatXList)):
        bulletcX.append(popcatXList[i-1])
        bulletcY.append(popcatYList[i-1])
        bulletdirect.append(random.randint(1,2))

#fonts
font1 = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('Creator_Campotype.otf', 50)

#Game instructions
controls = ["Game Controls:", "W: Move Up", "S: Move Down", "A: Move Right", "D: Move Left"]


def boundsX(x):
    if x <= 0:
        x = 0
    if x >= 830:
        x = 830
    return x


def boundsY(y):
    if y <= 0:
        y = 0
    if y >= 730:
        y = 730
    return y


def player(x, y, direction):
    screen.blit(playerCircle, (x - 10, y - 2))
    if direction == "left":
        screen.blit(playerImgL, (x, y))
    if direction == "right":
        screen.blit(playerImgR, (x, y))


def bongocat(x, y, frame):
    screen.blit(cloud, (x-15, y+30))
    if frame == 1:
        screen.blit(bongocat_f1, (x, y))
    if frame == 2:
        screen.blit(bongocat_f2, (x, y))


def popcat(x, y, frame):
    screen.blit(cloud, (x-40, y+50))
    if frame == 1:
        screen.blit(popcat_f1, (x, y))
    else:
        screen.blit(popcat_f2, (x, y))


def playerbullet(x, y):
    screen.blit(bulletp, (x, y))

def catbullet(x, y):
    screen.blit(bulletc, (x,y))


def collision(x1, x2, y1, y2):
    if ((x2 - x1) ** 2) + ((y2 - y1) ** 2) ** (1 / 2) <= 40:
        return True
    return False

def text(text, font, color, x, y):
    input = font.render(text, True, color)
    screen.blit(input, (x, y))

# Setting game loop
start = True
score = 0
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import main
            start = False
        if event.type == pygame.KEYDOWN:
            # if event.type == pygame.K_ESCAPE:
            #     import __main__
            if event.key == pygame.K_a:
                direction = "right"
                playerX -= 20
            if event.key == pygame.K_d:
                direction = "left"
                playerX += 20
            if event.key == pygame.K_w:
                playerY -= 20
            if event.key == pygame.K_s:
                playerY += 20


    # Setting screen background
    screen.fill((95, 0, 160))
    screen.blit(background, (0, 0))

    # calling player
    playerX = boundsX(playerX)
    playerY = boundsY(playerY)
    player(playerX, playerY, direction)
    for i in range(len(bulletp_XList)):
        playerbullet(bulletp_XList[i - 1], bulletp_YList[i - 1])
        bulletp_YList[i - 1] -= 20
    # Text
    scoreboard = "Score: " + str(score)
    text(scoreboard, font2, (0, 0, 0), 910, 10)
    for i in range(len(controls)):
        text(controls[i], font1, (0, 0, 0), 910, 90 + 20 * (i + 1))


    # bongo cat movements
    if bongoalive == True:
        score += 100
        if bongoX >= 786:
            bongoshift = -1
        if bongoX <= 0:
            bongoshift = 1
        bongoX = bongoX + bongoshift
        bongocat(bongoX, bongoY, random.randint(1, 2))
        # calling pop cat
        for i in range(len(popcatXList)):
            popcat(popcatXList[i - 1], popcatYList[i - 1], random.randint(1, 2))
        popcat_sound.play()

        #bullet mechanics
        for i in range(len(bulletp_XList)):
            for x in range(len(popcatXList)):
                if bulletp_YList[i-1] <= 0:
                    bulletp_XList[i-1] = playerX
                    bulletp_YList[i-1] = playerY

            for z in range(len(bulletcX)):
                for x in range(len(popcatXList)):
                    if bulletcX[z] <= 0 or bulletcX[z] >= 870 or bulletcY[z] <= 0 or bulletcY[z] >= 785:
                        bulletcX[z] = popcatXList[random.randint(0, len(popcatXList)-1)]
                        bulletcY[z] = popcatYList[random.randint(0, len(popcatXList)-1)]
                    else:
                        if bulletdirect[z-1] == 1:
                            bulletcX[z] += .05
                        else:
                            bulletcX[z] -= .05
                        bulletcY[z] += .05
                        catbullet(bulletcX[z] + 10, bulletcY[z] + 10)


            for x in range(len(popcatXList)):
                if popcatkills >= 10:
                    if collision(bulletp_XList[i - 1], bongoX, bulletp_YList[i - 1], bongoY) == True:
                        bongohealth -= 1
                        if bongohealth <= 0:
                            score += 10000
                            bongoalive = False



                if collision(bulletp_XList[i - 1], popcatXList[x-1], bulletp_YList[i-1], popcatYList[x-1]) == True:
                    popcathealth[x-1] -= 1
                    bulletp_XList[i - 1] = playerX
                    bulletp_YList[i - 1] = playerY
                    if popcathealth[x-1] <= 0:
                        score += 1000
                        popcatkills += 1
                        popcatXList.pop(x-1)
                        popcatYList.pop(x-1)
                        popcathealth.pop(x-1)
                        if popcatkills <= 5:
                            popcatXList.append(random.randint(0, 786))
                            popcatYList.append(170)
                            popcathealth.append(20)
                    if popcatkills >= 10:
                        popcatXList = []
                        popcatYList = []
                        popcathealth = []

    if bongoalive == False:
        text("You Won!" , font2, (0, 0, 0), 450, 400)

    clock.tick(40)
    pygame.display.update()
