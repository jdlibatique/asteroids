import pygame

from circleshape import CircleShape

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            self.position,
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt

        if self.position.x < 0 or self.position.x >= pygame.display.get_surface().get_width():
            self.kill()
            print("Shot out of bounds, removing shot.")

        if self.position.y < 0 or self.position.y >= pygame.display.get_surface().get_height():
            self.kill()
            print("Shot out of bounds, removing shot.")