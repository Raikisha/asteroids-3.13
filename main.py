import pygame
import constants
import player
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #console output before launching the game
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Launching with screen resolution:")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    #setting up clock and variables and player character
    gameclock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    playercharacter = player.Player(constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()


    #main game loop starts here

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        for thingy in drawable:
            thingy.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(playercharacter):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = (gameclock.tick(60)/1000)

        




if __name__ == "__main__":
    main()
