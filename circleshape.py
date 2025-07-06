from collections import defaultdict
from collections.abc import Collection

import pygame


class GroupCollection:
    registry = defaultdict(set)

    def __set_name__(self, _, name):
        self.name = name

    def __get__(self, instance, owner) -> set:
        if instance is not None:
            return self.registry[owner.__name__]
        return set()

    def __set__(self, instance, groups: Collection[pygame.sprite.Group]):
        if not all(isinstance(group, pygame.sprite.Group) for group in groups):
            raise ValueError(
                f"{instance.__class__.__name__}.{self.name} "
                "can only be a collection of `pygame.sprite.Group` objects"
            )
        self.registry[instance.__class__.__name__] = set(groups)


class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects"""

    containers = GroupCollection()

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(*self.__class__.containers)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        raise NotImplementedError

    def update(self, dt):
        raise NotImplementedError
