import logging
import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_OUT_OF_BOUNDS_TIME


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.out_of_bounds_time = 0

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            self.position,
            self.radius, 2
        )

    def update(self, delta_time):
        self.position += self.velocity * delta_time

        if self.is_out_of_bounds():
            self.out_of_bounds_time += delta_time
            if self.out_of_bounds_time > ASTEROID_MAX_OUT_OF_BOUNDS_TIME:
                logging.info("Asteroid out of bounds, removing asteroid.")
                self.kill()

    def is_out_of_bounds(self):
        return (self.position.x < 0 or self.position.x >= pygame.display.get_surface().get_width()
                or self.position.y < 0 or self.position.y >= pygame.display.get_surface().get_height())

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




