import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        raise NotImplementedError("Sub-classes must implement the draw method")

    def update(self, delta_time):
        # sub-classes must override
        raise NotImplementedError("Sub-classes must implement the update method")

    def is_collided(self, other):
        return (self.position.distance_to(other.position)
            <= (self.radius + other.radius))