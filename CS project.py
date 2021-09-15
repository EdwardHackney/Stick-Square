import pygame, random, time

# Window Setup
windowWidth = 800
windowHeight = 600
pygame.init()
win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

class Stickman:
    def __init__(self):
        self.x = x
        self.y = y
        self.radius = radius
        self.sprite = sprite
        self.vel = 0
        self.dead = False
        self.timeAlive = 0

class Square: 
    def __init__(self):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed




running = True

squares = []
deletedSquares = []

while running:
    #Window stuff
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((135, 206, 235))

    pygame.draw.rect(win, (255, 100, 0), (225, 225, 50, 50))

    pygame.display.update()

    #before starting to play
    pygame.draw.rect(win, (255, 100, 0), (225, 225, 50, 50))



pygame.quit()