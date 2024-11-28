import pygame

### import own files
from player import *
from constants import *

def main():

    ### initiate pygame and open screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ### opening game clock
    clock = pygame.time.Clock()
    dt = 0

    ### instantiate Player
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    ### game loop
    while(1):

        ### closing windows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ### blacken screen and draw player
        screen.fill(color="#000000")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()        

        ### limit FPS to 60 and get actual delta time
        dt = clock.tick(60)/1000


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()