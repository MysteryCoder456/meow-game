from random import randint, random

import pygame
from pygame import Vector2
from pygame.sprite import Group, spritecollide

from meow import Meow, MEOW_LAUNCH_STRENGTH
from mouse import Mouse

FPS = 60


def main():
    win = pygame.display.set_mode((928, 580))
    pygame.display.set_caption("Meow")
    win_size = Vector2(win.get_size())
    clock = pygame.time.Clock()

    # Custom events
    spawn_mouse_event = pygame.USEREVENT + 1

    # Game objects
    meow = Meow(win_size / 2)
    mice: Group[Mouse] = Group()  # type: ignore

    # Spawn a mouse every 3 seconds
    pygame.time.set_timer(spawn_mouse_event, 3000)

    while True:
        dt = clock.tick(FPS) / 1000

        # Event handling
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return

            elif ev.type == pygame.MOUSEBUTTONDOWN and meow.energy > 0:
                mouse_pos = Vector2(pygame.mouse.get_pos())
                meow_pos = Vector2(meow.rect.center)  # type: ignore
                dir = (mouse_pos - meow_pos).normalize()

                meow.velocity = dir * MEOW_LAUNCH_STRENGTH
                meow.energy -= 1

            elif ev.type == spawn_mouse_event:
                new_x = randint(0, int(win_size.x - 100)) + 50
                new_y = randint(0, int(win_size.y - 100)) + 50
                dir = (random() * 2 - 1) * 180

                mouse = Mouse(Vector2(new_x, new_y), dir)
                mice.add(mouse)

        # Update game objects
        meow.update(dt)
        mice.update(dt)

        # Edge collisions

        if meow.rect.left < 0:  # type: ignore
            meow.velocity.x *= -1
            meow.rect.left = 0  # type: ignore
        elif meow.rect.right > win_size.x:  # type: ignore
            meow.velocity.x *= -1
            meow.rect.right = win_size.x  # type: ignore

        if meow.rect.top < 0:  # type: ignore
            meow.velocity.y *= -1
            meow.rect.top = 0  # type: ignore
        elif meow.rect.bottom > win_size.y:  # type: ignore
            meow.velocity.y *= -1
            meow.rect.bottom = win_size.y  # type: ignore

        # Meow - mouse collisions
        if collided_mice := spritecollide(meow, mice, dokill=True):  # type: ignore
            num_of_mice = len(collided_mice)
            meow.score += num_of_mice
            meow.energy += num_of_mice

        # Draw game objects

        win.fill("black")

        meow.show(win)

        for mouse in mice:
            mouse.show(win)

        pygame.display.flip()


if __name__ == "__main__":
    main()
