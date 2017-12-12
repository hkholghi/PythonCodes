import pygame
from pygame.locals import *
import random
from sys import exit
from time import sleep

pygame.init()

display_width = 800
display_height = 600

# initial location of the ball
startx = random.randint(0,display_width)
starty = random.randint(0,display_height)



dx = 10
dy = 8

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)



game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.update()


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (
            event.type == KEYDOWN and (
            event.key == K_ESCAPE or
            event.key == K_q
            )):
            pygame.quit()
            quit()

while True:
    event_handler()
    game_display.fill(white)

    if startx > display_width or startx <= 0:
        dx = -dx

    if starty > display_height or starty <= 0:
        dy = -dy

    startx = startx + dx
    starty = starty + dy

    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    ballColor = (red,green,blue)

    pygame.draw.circle(game_display,ballColor,[startx,starty],10)
    sleep(.15)
    pygame.display.update()
