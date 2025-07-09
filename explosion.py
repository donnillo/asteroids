import pathlib
import random

import pygame

import constants
from constants import DEFAULT_SCREEN as SCREEN
from constants import Asteroid
from groups import Groupable, DRAWABLE, UPDATABLE


IMAGES = [*pathlib.Path("assets/explosion").glob("dust*")]


class Explosion(Groupable, pygame.sprite.Sprite, groups=(DRAWABLE, UPDATABLE)):
    const = constants.Explosion

    size2images: dict[int, list[pygame.surface.Surface]] = {
        size + 1: [
            pygame.transform.scale(
                pygame.image.load(img),
                (SCREEN.height / 15 * 1.3 ** size,) * 2
            ) for img in IMAGES
        ] for size in range(Asteroid.KINDS)
    }

    def __init__(self, at: pygame.math.Vector2, *, size: int):
        super().__init__(*self.__class__.containers)
        self.position = (int(at.x), int(at.y))
        self.size = size
        self.index = 0
        self.images = self.__class__.size2images[size]
        self.rotation: int = random.randint(0, 359)
        self.frame_timer = 0.0

    def draw(self, screen: pygame.surface.Surface):
        image = pygame.transform.rotate(self.images[self.index], self.rotation)
        rect = image.get_rect()
        rect.center = self.position
        screen.blit(image, rect)

    def update(self, dt):
        if self.frame_timer > self.const.FRAME_TIME / 1000:
            if self.index < self.const.NUM_FRAMES - 1:
                self.frame_timer = 0.0
                self.index += 1
            else:
                self.kill()
        else:
            self.frame_timer += dt
