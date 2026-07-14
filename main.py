import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clockObj = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    Shot.containers = (shots, updatable,drawable)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        dt = clockObj.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            collision = asteroid.collides_with(player)
            if collision == True:
                log_event("player_hit")
                print("Game Over")
                sys.exit()
            for shot in shots:
                collision_shot = asteroid.collides_with(shot)
                if collision_shot == True:
                    # Log an event when an asteroid is hit by a shot
                    try:
                        log_event(
                            "asteroid_shot",
                            asteroid_pos=[round(asteroid.position.x, 2), round(asteroid.position.y, 2)],
                            shot_pos=[round(shot.position.x, 2), round(shot.position.y, 2)],
                        )
                    except Exception:
                        # Fall back to a simple event if positions aren't available
                        log_event("asteroid_shot")

                    asteroid.split()
                    shot.kill()


if __name__ == "__main__":
    main()
