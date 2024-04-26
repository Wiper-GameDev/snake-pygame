from __future__ import annotations
from functools import cached_property
import typing
from pygame import Surface
import pygame
from objects.food import Food
from objects.snake import Snake
from scenes.base_scene import BaseScene

if typing.TYPE_CHECKING:
    from game import Game  

class GameScene(BaseScene):
    def __init__(self, game: Game):
        super().__init__(game)
        self.TILE_SIZE = 40
        self.snake = Snake()
        self.snake.layer = 1
        self.add_object(self.snake)
        self.food = Food()
        self.add_object(self.food)
        self.paused = False
        

    def draw(self, screen: Surface):
        super().draw(screen)
        font = pygame.font.SysFont("arial", 32)
        fps = self.game.clock.get_fps()
        surface = font.render(f"{fps:.0f}", True, (0, 255, 0))
        screen.blit(surface, (600, 20))

    def handle_event(self, event: pygame.Event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # self.game.set_scene(0)
            self.paused = not self.paused



    def update(self, delta: float):
        if self.paused:
            return
        
        super().update(delta)
        if self.snake.rect.colliderect(self.food.rect):
            print(f"Eaten {delta}")
            self.food.destroy()
            self.food = Food()
            self.add_object(self.food)
            self.snake.grow()

            
