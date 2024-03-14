import pygame
from pygame import Vector2

from meow import Meow, MEOW_LAUNCH_STRENGTH

FPS = 60


def main():
    win = pygame.display.set_mode((928, 580))
    pygame.display.set_caption("Meow")
    win_size = Vector2(win.get_size())
    clock = pygame.time.Clock()

    meow = Meow(win_size / 2)

    while True:
        dt = clock.tick(FPS) / 1000

        # Event handling
        for ev in pygame.event.get():
            match ev.type:
                case pygame.QUIT:
                    return

                case pygame.MOUSEBUTTONDOWN:
                    mouse_pos = Vector2(pygame.mouse.get_pos())
                    meow_pos = Vector2(meow.rect.center)
                    dir = (mouse_pos - meow_pos).normalize()
                    meow.velocity = dir * MEOW_LAUNCH_STRENGTH

        # Update game objects
        meow.update(dt)

        # Edge collisions

        if meow.rect.left < 0:
            meow.velocity.x *= -1
            meow.rect.left = 0
        elif meow.rect.right > win_size.x:
            meow.velocity.x *= -1
            meow.rect.right = win_size.x

        if meow.rect.top < 0:
            meow.velocity.y *= -1
            meow.rect.top = 0
        elif meow.rect.bottom > win_size.y:
            meow.velocity.y *= -1
            meow.rect.bottom = win_size.y

        # Draw game objects
        win.fill("black")
        meow.show(win)
        pygame.display.flip()


if __name__ == "__main__":
    main()
