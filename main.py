import pygame
import sys

### import own files
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    ### initiate pygame and open screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ### opening game clock
    clock = pygame.time.Clock()
    dt = 0

    ### instantiate groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    ### instantiate asteroidfield and add to groups
    AsteroidField.containers = (updateable)
    a_field = AsteroidField()

    ### add asteroids to groups
    Asteroid.containers = (updateable, drawable, asteroids)

    ### add shots to groups
    Shot.containers = (updateable, drawable, shots)

    ### instantiate Player and add to groups
    Player.containers = (updateable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    

    ### game loop
    while(1):

        ### closing windows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ### adjust screen - black, update sprites, draw sprites, flip
        screen.fill(color="#000000")
        for sprite in updateable:
            sprite.update(dt)
        for asteroid in asteroids:

            ### checks for player collision
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit("You've been hit by an asteroid. Game over!")
            
            ### checks for shot collision
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()        

        ### limit FPS to 60 and get actual delta time
        dt = clock.tick(60)/1000


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()