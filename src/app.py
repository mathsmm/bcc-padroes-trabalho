import pygame as pg
from pygame.locals import *
from src.vec2 import Vec2
from src.body_behavior import *
from src.circle_body import CircleBody
from src.rect_body import RectBody
from src.collision_logic import CollisionLogic

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
        # PREPARAR LISTA DE CORPOS
        b1 = CircleBody(Vec2(50, 50), Vec2(15, 25), Vec2(0, 0), 40, 10)
        b1.move_behav = DoMove(b1)
        b1.vel_display_behav = DoDisplayVel(self.screen, b1)
        b1.body_display_behav = DisplayCircle(self.screen, b1)

        b2 = RectBody(Vec2(250, 400), Vec2(10, 5), Vec2(0, 0), 40, 30, 70)
        b2.move_behav = DontMove()
        b2.vel_display_behav = DontDisplayVel()
        b2.body_display_behav = DisplayRect(self.screen, b2)
        
        self.bodies.append(b1)
        self.bodies.append(b2)

        # CRIAR OBJETO ITERADOR
        # TODO

        while self.running:
            self.screen.fill((0, 0, 0))
            self.handle_events()
            self.loop_bodies()
            
            # pg.draw.line(self.screen, line_color, (60, 80), (130, 100))
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
        for b1 in self.bodies:
            # for b2 in self.bodies
            b1.move(0.005)
            b1.display((255, 0, 0))
            b1.display_vel((0, 255, 0))

            for b2 in self.bodies:
                if b1 == b2:
                    continue

                if type(b1) is CircleBody   and type(b2) is CircleBody:
                    CollisionLogic.circle_circle_collision(b1, b2)
                elif type(b1) is CircleBody and type(b2) is RectBody:
                    CollisionLogic.circle_rect_collision(b1, b2)
                elif type(b1) is RectBody   and type(b2) is CircleBody:
                    CollisionLogic.circle_rect_collision(b2, b1)
                elif type(b1) is RectBody   and type(b2) is RectBody:
                    pass