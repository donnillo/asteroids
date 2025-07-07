import pygame

import shapes
import constants
from constants import Color
from groups import ASTEROIDS, UPDATABLE, DRAWABLE


class Asteroid(shapes.Circle, groups=(ASTEROIDS, UPDATABLE, DRAWABLE)):
    const = constants.Asteroid

    def draw(self, screen):
        pygame.draw.circle(screen, Color.WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
