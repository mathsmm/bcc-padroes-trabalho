import pygame

class TimeHandler:
    def __init__(self, fps) -> None:
        self.fps = fps
        self.ticks = 0
        self.dDT = 1000.0 / fps
        self.dT = 0
        self.rDT = 0.0

    def wait(self):
        self.dT = pygame.time.get_ticks() - self.ticks

        if self.dT < self.dDT:
            pygame.time.wait(int(self.dDT - self.dT))

        self.rDT = (pygame.time.get_ticks() - self.ticks) / 1000.0