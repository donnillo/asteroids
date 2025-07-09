import pygame

from groups import Groupable


class Circle(Groupable, pygame.sprite.Sprite):
    """Base class for game objects"""

    def __init__(self, at: pygame.math.Vector2, /, radius: float):
        super().__init__(*self.__class__.containers)
        self.position: pygame.math.Vector2 = pygame.math.Vector2(at.x, at.y)
        self.velocity: pygame.math.Vector2 = pygame.math.Vector2(0, 0)
        self.radius = radius

    def is_colliding(self, other: "Circle") -> bool:
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def draw(self, screen):
        raise NotImplementedError

    def update(self, dt):
        raise NotImplementedError
