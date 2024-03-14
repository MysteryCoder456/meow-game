from pathlib import Path

import pygame
from pygame import Vector2
from pygame.transform import scale_by

MEOW_IMAGE_PATH = Path(__file__).parent.parent / "assets" / "meow.png"
MEOW_LAUNCH_STRENGTH = 1500
MEOW_VELOCITY_DAMPING = 0.02


class Meow:
    """
    A meow. Also the main character.
    """

    def __init__(self, position: Vector2):
        self._image = pygame.image.load(MEOW_IMAGE_PATH)
        self._image = scale_by(self._image, 2)

        self.velocity = Vector2()
        self.rect = pygame.FRect(self._image.get_rect())
        self.rect.center = position

    def update(self, dt):
        self.velocity *= 1 - MEOW_VELOCITY_DAMPING
        self.rect = self.rect.move(self.velocity * dt)

    def show(self, surface: pygame.Surface):
        surface.blit(self._image, self.rect.topleft)
