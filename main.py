import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="#000000")
        pygame.display.flip()



        dt = clock.tick(60)/1000


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()