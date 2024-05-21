from vec2 import Vec2

class Body:
    def __init__(
        self,
        init_pos: Vec2,
        init_vel: Vec2,
        init_accel: Vec2,
        mass: float
    ) -> None:
        self.pos: Vec2 = init_pos
        self.vel: Vec2 = init_vel
        self.acc: Vec2 = init_accel
        self.mass: float = mass
        self.move_behav = None