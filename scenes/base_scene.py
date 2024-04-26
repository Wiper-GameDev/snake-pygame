from __future__ import annotations
import typing
from pygame import Surface
import pygame

from objects.base_object import BaseObject


if typing.TYPE_CHECKING:
    from game import Game


class BaseScene:
    def __init__(self, game: Game):
        self.game = game
        self.objects: typing.Set[BaseObject] = set()

    def handle_event(self, event: pygame.Event):
        for o in self.objects:
            o.handle_event(event)

    def update(self, delta: float):
        for o in self.objects:
            o.update(delta)

    def draw(self, screen: Surface):
        for o in sorted(self.objects, key=lambda o: o.layer):
            o.draw(screen)

    def add_object(self, object: BaseObject):
        object.scene = self
        self.objects.add(object)

    def remove_object(self, object: BaseObject):
        self.objects.remove(object)
