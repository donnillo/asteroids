import enum

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


class Screen(NumericConstant):
    WIDTH = 1280
    HEIGHT = 720

    class Size:
        def __get__(self, _, owner):
            return pygame.math.Vector2(owner.WIDTH, owner.HEIGHT)

    class Center:
        def __get__(self, _, owner):
            return pygame.math.Vector2(owner.WIDTH / 2, owner.HEIGHT / 2)

    size = Size()
    center = Center()


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
