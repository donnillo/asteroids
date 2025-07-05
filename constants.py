import enum


class Constant(enum.Enum):
    def __repr__(self):
        return "{} {}: {}".format(
            self.__class__.__name__,
            self.name.replace("_", " ").lower(),
            self.value
        )

    __str__ = __repr__


class Screen(int, Constant):
    WIDTH = 1280
    HEIGHT = 720


class Asteroid(Constant):
    MIN_RADIUS = 20
    KINDS = 3
    SPAWN_RATE = 0.8  # seconds
    MAX_RADIUS = MIN_RADIUS * KINDS
