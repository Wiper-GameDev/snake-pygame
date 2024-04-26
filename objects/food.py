import random
from pygame import Surface
import pygame
from objects.base_object import BaseObject


class Food(BaseObject):
    def __init__(self) -> None:
        super().__init__()
        self.r = 10
        self.rect = pygame.Rect(
            random.randint(0, 800) - self.r, random.randint(0, 600) - self.r, self.r * 2, self.r * 2
        )

    def update(self, delta: float):
        return super().update(delta)

    def draw(self, screen: Surface):
        pygame.draw.circle(screen, (255, 0, 0), (self.rect.x + self.r, self.rect.y + self.r), self.r)
        return super().draw(screen)
