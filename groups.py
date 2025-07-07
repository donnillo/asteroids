from abc import ABC
from collections import defaultdict
from collections.abc import Collection
from typing import Optional

import pygame


UPDATABLE = pygame.sprite.Group()
DRAWABLE = pygame.sprite.Group()
ASTEROIDS = pygame.sprite.Group()


class GroupCollection:
    registry = defaultdict(set)

    def __get__(self, _, owner) -> set[pygame.sprite.Group]:
        return self.registry[owner.__name__]


class Groupable(ABC):
    containers = GroupCollection()

    def __init_subclass__(cls, groups: Optional[Collection[pygame.sprite.Group]] = None):
        if groups:
            cls.containers.update(groups)
