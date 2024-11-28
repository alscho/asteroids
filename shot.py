from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#FF0000", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt    