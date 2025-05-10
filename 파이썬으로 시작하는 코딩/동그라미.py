import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("First program")
screen = pygame.display.set_mode((640, 480))
xpos = 50
clock = pygame.time.Clock()
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_RIGHT]:
        xpos += 10
    if pressed_keys[K_LEFT]:
        xpos -= 10
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 255, 0), (xpos, 200), 20)
    pygame.display.update()