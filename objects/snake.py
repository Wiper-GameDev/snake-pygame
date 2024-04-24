from pygame import Surface, Vector2
import pygame
from objects.base_object import BaseObject


class Snake(BaseObject):
    def __init__(self) -> None:
        super().__init__()
        self.size = 20
        self.speed = 40
        self.direction = Vector2(1, 0)
        self.position = Vector2(300, 300)

    def update(self, delta: float):
        super().update(delta)
        self.position += self.speed * delta * self.direction
    

    def draw(self, screen: Surface):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            pygame.Rect(self.position.x, self.position.y, self.size, self.size),
        )
