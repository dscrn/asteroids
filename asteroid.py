import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(25, 50)
            split_vector_one = self.velocity.rotate(random_angle)
            split_vector_two = self.velocity.rotate(-1 * random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = split_vector_one * 1.2
            asteroid_b.velocity = split_vector_two * 1.2
