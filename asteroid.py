import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        random_angle = random.uniform(20, 50)
        new_velocity = [
            self.velocity.rotate(random_angle),
            self.velocity.rotate(-random_angle)
        ]
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        for i in range(0, 2):
            asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid.velocity = new_velocity[i]*1.2
        
        self.kill()
        

