import sys

import pygame

from constants import DEFAULT_SCREEN as SCREEN
from constants import Color
from player import Player
from asteroidfield import AsteroidField
from groups import UPDATABLE, DRAWABLE, SHOTS
from groups import GenericGroup
from shot import Shot


def main():
    screen = pygame.display.set_mode(SCREEN.size)
    clock = pygame.time.Clock()
    player = Player(at=SCREEN.center)
    asteroids = AsteroidField.populate()
    shots: GenericGroup[Shot] = SHOTS

    while True:
        screen.fill(Color.BLACK)
        for sprite in DRAWABLE:
            sprite.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        UPDATABLE.update(clock.tick(60) / 1000)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                sys.exit(1)
            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.explode(asteroid)


if __name__ == "__main__":
    main()
