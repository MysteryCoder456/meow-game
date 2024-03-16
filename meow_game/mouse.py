from pathlib import Path

import pygame
from pygame import Vector2
from pygame.transform import scale_by, flip

MOUSE_IMAGE_PATH = Path(__file__).parent.parent / "assets" / "mouse.png"
MOUSE_SPEED = 65


class Mouse(pygame.sprite.Sprite):
    """
    A mouse. Also the antagonist!
    """

    def __init__(self, position: Vector2, direction: float):
        super().__init__()

        self._image = pygame.image.load(MOUSE_IMAGE_PATH)
        self._image = scale_by(self._image, 1.5)

        self.velocity = Vector2()
        self.velocity.from_polar((MOUSE_SPEED, direction))

        self.rect = pygame.FRect(self._image.get_rect())
        self.rect.center = position

    def update(self, dt: float):  # type: ignore
        self.rect = self.rect.move(self.velocity * dt)  # type: ignore

    def show(self, surface: pygame.Surface):
        img = flip(self._image, self.velocity.x < 0, False)
        surface.blit(img, self.rect.topleft)  # type: ignore
