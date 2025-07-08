from abc import ABC
from collections import defaultdict
from collections.abc import Collection
from collections.abc import Iterator
from typing import Optional

import pygame


UPDATABLE = pygame.sprite.Group()
DRAWABLE = pygame.sprite.Group()


class GenericGroup[S: pygame.sprite.Sprite](pygame.sprite.Group):
    def __iter__(self) -> Iterator[S]:
        return super().__iter__()


ASTEROIDS: GenericGroup = GenericGroup()
SHOTS: GenericGroup = GenericGroup()


class GroupCollection:
    registry = defaultdict(set)

    def __get__(self, _, owner) -> set[pygame.sprite.Group]:
        return self.registry[owner.__name__]


class Groupable(ABC):
    containers = GroupCollection()

    def __init_subclass__(cls, groups: Optional[Collection[pygame.sprite.Group]] = None):
        if groups:
            cls.containers.update(groups)
