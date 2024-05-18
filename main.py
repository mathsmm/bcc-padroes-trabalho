import pygame as pg
from pygame.locals import *

pg.init() 

width = 1000
height = 500

screen_color = (49, 150, 100)
line_color = (255, 0, 0)

screen = pg.display.set_mode((width,height))
screen.fill(screen_color)

running = True

while running:

    for event in pg.event.get():

        if event.type == KEYDOWN:

            if event.key == K_BACKSPACE:
                running = False

        # Check for QUIT event
        elif event.type == QUIT:
            running = False

    pg.draw.line(screen,line_color, (60, 80), (130, 100))
    pg.display.flip()