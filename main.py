import sys

import pygame

from constants import DEFAULT_SCREEN as SCREEN
from constants import Color
from player import Player
from asteroidfield import AsteroidField
from groups import UPDATABLE, DRAWABLE


def main():
    screen = pygame.display.set_mode(SCREEN.size)
    clock = pygame.time.Clock()
    player = Player(at=SCREEN.center)
    asteroids = AsteroidField.populate()

    while True:
        screen.fill(Color.BLACK)
        for sprite in DRAWABLE:
            sprite.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        UPDATABLE.update(clock.tick(60) / 1000)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                sys.exit(1)


if __name__ == "__main__":
    main()
