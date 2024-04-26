from __future__ import annotations
from functools import cached_property
from typing import List, TYPE_CHECKING, Type, override
from pygame import Surface, Vector2
import pygame
from objects.base_object import BaseObject

# from scenes.game_scene import GameScene

if TYPE_CHECKING:
    from scenes.game_scene import GameScene


class Snake(BaseObject):
    scene: GameScene  # type: ignore

    def __init__(self) -> None:
        super().__init__()
        self.speed = 10
        # self.speed = 120
        self.direction = Vector2(1, 0)
        self.upcoming_turn = None
        self.parts: List[Vector2] = [
            # Vector2(15, 15),
            # Vector2(14, 15),
            # Vector2(13, 15),
            # Vector2(12, 15),
        ]
        self._diff = Vector2()
        self._extra_head_added = False
        for i in range(10):
            self.parts.append(Vector2(15 - i, 15))

    def update(self, delta: float):
        super().update(delta)
        self.move(delta)

    def move(self, delta: float):
        self._diff += self.direction * delta * self.speed


        if abs(self._diff.x) >= 1 or abs(self._diff.y) >= 1:
            if self.upcoming_turn:
                self.direction = self.upcoming_turn
                self.upcoming_turn = None

            self._dummy_head = None
            self.parts.insert(0, self.parts[0] + self._diff)
            self.parts.pop()
            self._diff = Vector2()
        else:
            self._dummy_head = self.parts[0] + self._diff

        


        # if self._extra_head_added:
        #     print(self._extra_head_added)
        #     self.parts[0] += self.direction * delta * 4
        
        # if max_diff > 1 and self._extra_head_added:
        #     self.parts.pop()
        #     self._extra_head_added = False



    @property
    def rect(self):
        rect = self._dummy_head if self._dummy_head else self.parts[0]
        return pygame.Rect(
            rect * self.scene.TILE_SIZE,
            (self.scene.TILE_SIZE, self.scene.TILE_SIZE),
        )

    def handle_event(self, event: pygame.Event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.upcoming_turn = Vector2(1, 0)
            elif event.key == pygame.K_a:
                self.upcoming_turn = Vector2(-1, 0)
            elif event.key == pygame.K_s:
                self.upcoming_turn = Vector2(0, 1)
            elif event.key == pygame.K_w:
                self.upcoming_turn = Vector2(0, -1)

    def draw(self, screen: Surface):
        def draw_segment(index: int, part: Vector2):
            surface = pygame.Surface(
                (self.scene.TILE_SIZE, self.scene.TILE_SIZE), pygame.SRCALPHA
            )
            min_alpha = 50
            alpha = min(
                round(
                    min_alpha
                    + (255 - min_alpha) * (len(self.parts) - index) / len(self.parts)
                ),
                255,
            )
            border_size = 1
            pygame.draw.rect(
                surface,
                (
                    255,
                    255,
                    255,
                    alpha,
                ),
                pygame.Rect(
                    0,
                    0,
                    self.scene.TILE_SIZE,
                    self.scene.TILE_SIZE,
                ),
            )

            pygame.draw.rect(
                surface,
                (0, 0, 255, alpha),
                (
                    border_size,
                    border_size,
                    self.scene.TILE_SIZE - border_size * 2,
                    self.scene.TILE_SIZE - border_size * 2,
                ),
            )

            screen.blit(
                surface,
                (
                    part.x * self.scene.TILE_SIZE,
                    part.y * self.scene.TILE_SIZE,
                ),
            )


        i = 0
        if self._dummy_head:
            i = 1
            draw_segment(0, self._dummy_head)

        for i, part in enumerate(self.parts, start=i):
            draw_segment(i, part)

    def grow(self):
        self.parts.append(self.parts[-1] - self.direction)