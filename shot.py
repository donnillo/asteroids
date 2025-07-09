import pygame

import shapes
import constants
from constants import Color
from groups import SHOTS, UPDATABLE, DRAWABLE
from explosion import Explosion
from asteroid import Asteroid


class Shot(shapes.Circle, groups=(SHOTS, UPDATABLE, DRAWABLE)):
    const = constants.Shot

    def __init__(self, at):
        super().__init__(at, radius=self.const.RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, Color.WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def explode(self, asteroid: Asteroid):
        self.kill()
        asteroid.split()
        Explosion((self.position + asteroid.position) / 2, size=asteroid.kind)
