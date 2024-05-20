import pygame
from pygame.locals import *

class Vec2:
    def __init__(self, x, y) -> None:
        if (type(x) is float) and (type(y) is float):
            self.x: float = x
            self.y: float = y
        elif (type(x) is Vec2) and (type(y) is Vec2):
            self.x = x.x + y.x
            self.y = x.y + y.y
        else:
            raise Exception("Vec2: wrong args")
    
    def module(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def set_module(self, mod: float):
        k = mod / self.module()
        self.x = self.x * k
        self.y = self.y * k

    def unit(self):
        return Vec2(self.x, self.y) / self.module()
    
    def s_distance_between(v1, v2):
        return Vec2(v1, v2).Module()