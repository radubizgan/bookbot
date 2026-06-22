import pygame
from constants import  SCREEN_WIDTH, SCREEN_HEIGHT 
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clockObj = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            pass
            if event.type == pygame.QUIT:
             return
        screen.fill("black")
        pygame.display.flip()
        dt = clockObj.tick(60) / 1000

if __name__ == "__main__":
    main()
