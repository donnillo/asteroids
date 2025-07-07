import enum
from typing import NamedTuple

import pygame


class NumericConstant(float, enum.Enum):
    def __str__(self):
        return "{} {}: {}".format(
            self.__class__.__name__,
            self.name.replace("_", " ").lower(),
            repr(self)
        )

    def __repr__(self):
        return f"{self.value:.6f}".rstrip("0").rstrip(".")


class Resolution(NamedTuple):
    width: int
    height: int

    @property
    def size(self):
        return pygame.math.Vector2(self.width, self.height)

    @property
    def center(self):
        return self.size / 2

    def __repr__(self):
        return f"{self.width}x{self.height}"


class Screen(Resolution, enum.Enum):
    HD = 1280, 720
    FullHD = 1920, 1080


class Asteroid(NumericConstant):
    MIN_RADIUS = 20
    KINDS = 3
    SPAWN_RATE = 0.8  # seconds
    MAX_RADIUS = MIN_RADIUS * KINDS


class Player(NumericConstant):
    RADIUS = 20
    TURN_SPEED = 300
    SPEED = 200


class Color(pygame.Color, enum.Enum):
    BLACK = "black"
    WHITE = "white"
