import pygame

import shapes
import constants
from constants import Color
from groups import SHOTS, UPDATABLE, DRAWABLE


class Shot(shapes.Circle, groups=(SHOTS, UPDATABLE, DRAWABLE)):
    const = constants.Shot

    def __init__(self, at):
        super().__init__(at, radius=self.const.RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, Color.WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
