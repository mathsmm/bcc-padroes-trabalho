import pygame as pg
from pygame.locals import *

class App:
    def __init__(
        self, 
        fps: int,
        window_width: int, 
        window_height: int
    ) -> None:
        self.running = False
        self.fps = fps
        self.window_width = window_width
        self.window_heigth = window_height

        # Bodies
        self.bodies = []
        self.circ_vtx_qty = 24

        # pygame
        pg.init()
        self.screen = pg.display.set_mode((window_width, window_height))

    def init(self):
        self.running = True
        self.start_main_loop()
        pg.quit()

    def start_main_loop(self):
        screen_color = (0, 0, 0)
        line_color = (255, 0, 0)
        # PREPARAR LISTA DE CORPOS
        # CRIAR OBJETO ITERADOR

        while self.running:
            self.screen.fill(screen_color)
            self.handle_events()
            self.loop_bodies()
            
            pg.draw.line(self.screen, line_color, (60, 80), (130, 100))
            pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == KEYDOWN:

                if event.key == K_BACKSPACE:
                    self.running = False

            # Check for QUIT event
            elif event.type == QUIT:
                self.running = False

    def loop_bodies(self):
        # CRIAR ITERADOR PRA ISTO
        # for b1 in self.bodies:
        #     for b2 in self.bodies:
        #         if b1 == b2: continue
        pass