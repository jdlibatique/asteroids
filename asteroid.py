import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            self.position,
            self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(random_angle)
        vector_b = self.velocity.rotate(-random_angle)

        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(
            self.position.x,
            self.position.y,
            new_asteroid_radius
        )

        asteroid_b = Asteroid(
            self.position.x,
            self.position.y,
            new_asteroid_radius
        )

        asteroid_a.velocity = vector_a * 1.2
        asteroid_b.velocity = vector_b * 1.2




