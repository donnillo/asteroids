import pygame

from constants import DEFAULT_SCREEN as SCREEN
from constants import Color
from player import Player


def main():
    screen = pygame.display.set_mode(SCREEN.size)
    clock = pygame.time.Clock()
    player = Player(at=SCREEN.center)

    while True:
        screen.fill(Color.BLACK)
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        player.update(dt)


if __name__ == "__main__":
    main()
