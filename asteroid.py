import random

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

    def split(self):
        self.kill()
        if self.radius > self.const.MIN_RADIUS:
            angle = random.uniform(20, 50)
            smaller_radius = self.radius - self.const.MIN_RADIUS
            for sign in (-1, 1):
                fragment = self.__class__(self.position, radius=smaller_radius)
                fragment.velocity = self.velocity.rotate(sign * angle) * 1.2
