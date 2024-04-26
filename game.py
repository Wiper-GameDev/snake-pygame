import pygame
from typing import List
from scenes.base_scene import BaseScene
from scenes.game_scene import GameScene
from scenes.main_menu_scene import MainMenuScene

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.SRCALPHA)
        self.running = True
        self.scenes: List[BaseScene] = [MainMenuScene(self), GameScene(self)]
        self.scene_idx = 0
        self.clock = pygame.Clock()

    @property
    def scene(self):
        return self.scenes[self.scene_idx]
    
    def set_scene(self, idx: int):
        self.scene_idx = idx

    def start(self):
        while self.running:
            delta = self.clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return

                self.scene.handle_event(event)

            self.screen.fill((0, 0, 0))
            self.scene.update(delta / 1000)
            self.scene.draw(self.screen)
            pygame.display.update()