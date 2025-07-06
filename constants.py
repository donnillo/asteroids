import enum

import pygame


class NumericConstant(float, enum.Enum):
    def __repr__(self):
        return "{} {}: {}".format(
            self.__class__.__name__,
            self.name.replace("_", " ").lower(),
            self.value
        )

    __str__ = __repr__


class Screen(NumericConstant):
    WIDTH = 1280
    HEIGHT = 720

    class Size:
        def __get__(self, _, owner) -> tuple[float, float]:
            return owner.WIDTH, owner.HEIGHT

    size = Size()


class Asteroid(NumericConstant):
    MIN_RADIUS = 20
    KINDS = 3
    SPAWN_RATE = 0.8  # seconds
    MAX_RADIUS = MIN_RADIUS * KINDS


class Player(NumericConstant):
    RADIUS = 20
    TURN_SPEED = 300


class Color(pygame.Color, enum.Enum):
    BLACK = "black"
    WHITE = "white"
