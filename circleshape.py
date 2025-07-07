import pygame

from groups import Groupable


class CircleShape(Groupable, pygame.sprite.Sprite):
    """Base class for game objects"""

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(*self.__class__.containers)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        raise NotImplementedError

    def update(self, dt):
        raise NotImplementedError
