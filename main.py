import pygame
import constants
import player
from logger import log_state
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

    playercharacter = player.Player(constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2)

    #main game loop starts here

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        playercharacter.update(dt)
        playercharacter.draw(screen)

        pygame.display.flip()
        dt = (gameclock.tick(60)/1000)

        




if __name__ == "__main__":
    main()
