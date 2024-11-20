import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print('Screen width: ' + str(SCREEN_WIDTH))
    print('Screen height: ' + str(SCREEN_HEIGHT))
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # assign classes to groups
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)

    # initalize objects
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.isColliding(shot):
                    shot.kill()
                    asteroid.split()
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
