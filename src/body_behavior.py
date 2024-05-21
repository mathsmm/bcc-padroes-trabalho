from abc import ABC, abstractmethod
import pygame
from pygame.locals import *
from pygame import Surface
from body import Body
from vec2 import Vec2

PI_MINUS_PI_DIV_6 = 2.6179938779914943653855361527329
PI_PLUS_PI_DIV_6 = 3.6651914291880921115397506138261

class MovementBehav(ABC):
    @abstractmethod
    def move(self, rDT):
        pass

class DoMove(MovementBehav):
    def __init__(self, b: Body) -> None:
        self.b = Body
    def move(self, rDT):
        # Accelerate then move
        self.b.vel = self.b.vel + (self.b.acc * rDT)
        self.b.pos = self.b.pos + (self.b.vel * rDT)

class DontMove(MovementBehav):
    def __init__(self) -> None:
        pass
    def move(self, rDT):
        pass

class VelDisplayBehav(ABC):
    @abstractmethod
    def display(self, surface: Surface, color: tuple):
        pass

class DoDisplayVel(VelDisplayBehav):
    def __init__(self, b: Body) -> None:
        self.b = b
    def display(self, surface: Surface, color: tuple):
        arrow_mod = self.b.vel.module() * 0.10
        l_arrow_segment = (self.b.vel.unit() * arrow_mod).rotate(PI_MINUS_PI_DIV_6)
        r_arrow_segment = (self.b.vel.unit() * arrow_mod).rotate(PI_PLUS_PI_DIV_6)
        pygame.draw.line(
            self.screen, color, 
            self.b.pos.coordinate(), 
            self.b.vel.coordinate()
        )
        arrow_initial_pos = self.b.pos + self.b.vel
        pygame.draw.line(
            self.screen, color, 
            arrow_initial_pos.coordinate(), 
            (arrow_initial_pos + l_arrow_segment).coordinate()
            # (arrow_initial_pos.x + l_arrow_segment.x, arrow_initial_pos.y + l_arrow_segment.y)
        )
        pygame.draw.line(
            self.screen, color, 
            arrow_initial_pos.coordinate(), 
            (arrow_initial_pos + r_arrow_segment).coordinate()
            # (arrow_initial_pos.x + r_arrow_segment.x, arrow_initial_pos.y + r_arrow_segment.y)
        )
        
class DontDisplayVel(VelDisplayBehav):
    def __init__(self) -> None:
        pass
    def display(self, surface: Surface, color: tuple):
        pass 

class BodyDisplayBehav(ABC):
    @abstractmethod
    def display(self):
        pass

class DoDisplayBody(BodyDisplayBehav):
    def __init__(self) -> None:
        pass
    def display(self, rDT):
        pass 

class DontDisplayBody(BodyDisplayBehav):
    def __init__(self) -> None:
        pass
    def display(self, rDT):
        pass 

# class CollisionBehav(ABC):
#     @abstractmethod
#     def collide(self):
#         pass

# class CollisionDetectionBehav(ABC):
#     @abstractmethod
#     def is_colliding(self):
#         pass