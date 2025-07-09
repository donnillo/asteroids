import enum
from typing import NamedTuple

import pygame


class NumericConstant(enum.IntEnum):
    def __str__(self):
        return f"{self.__class__.__name__}.{self.name}: {self.value}"


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


DEFAULT_SCREEN = Screen.HD


class Asteroid(NumericConstant):
    MIN_RADIUS = 20
    KINDS = 3
    SPAWN_RATE = 800  # milliseconds
    MAX_RADIUS = MIN_RADIUS * KINDS


class Player(NumericConstant):
    RADIUS = 20
    TURN_SPEED = 300
    SPEED = 200
    SHOT_SPEED = 500
    SHOOT_COOLDOWN = 300  # milliseconds


class Shot(NumericConstant):
    RADIUS = 5


class Explosion(NumericConstant):
    NUM_FRAMES = 7
    FRAME_TIME = 70  # milliseconds


class Color(pygame.Color, enum.Enum):
    BLACK = "black"
    WHITE = "white"
