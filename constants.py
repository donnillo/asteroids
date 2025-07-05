import enum


class Constant(enum.Enum):
    def __repr__(self):
        return f"{self.__class__.__name__} {self.name.lower()}: {self.value}"

    __str__ = __repr__


class Screen(Constant):
    WIDTH = 1280
    HEIGHT = 720


class Asteroid(Constant):
    MIN_RADIUS = 20
    KINDS = 3
    SPAWN_RATE = 0.8  # seconds
    MAX_RADIUS = MIN_RADIUS * KINDS
