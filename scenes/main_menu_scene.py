from pygame import Surface
import pygame
from scenes.base_scene import BaseScene


class MainMenuScene(BaseScene):
    def draw(self, screen: Surface):
        pygame.draw.rect(screen, (255, 255, 0), (25, 25, 25, 25))

    def handle_event(self, event: pygame.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.game.set_scene(1)
