from __future__ import annotations
import typing
from pygame import Surface
import pygame
from objects.snake import Snake
from scenes.base_scene import BaseScene

if typing.TYPE_CHECKING:
    from game import Game  

class GameScene(BaseScene):

    def __init__(self, game: Game):
        super().__init__(game)
        snake = Snake()
        self.add_object(snake)

    def draw(self, screen: Surface):
        super().draw(screen)
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 25, 25))
        font = pygame.font.SysFont("arial", 32)
        fps = self.game.clock.get_fps()
        surface = font.render(f"{fps:.0f}", True, (0, 255, 0))
        screen.blit(surface, (600, 20))

    def handle_event(self, event: pygame.Event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.game.set_scene(0)
            
