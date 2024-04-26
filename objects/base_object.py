from __future__ import annotations
from pygame import Surface, Event
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from scenes.base_scene import BaseScene


class BaseObject:
    scene: BaseScene
    layer = 0
    __destroyed = False

    def __init__(self) -> None:
        self.id = uuid.uuid4()

    def update(self, delta: float):
        pass

    def draw(self, screen: Surface):
        pass

    def handle_event(self, event: Event):
        pass

    def __eq__(self, value: object) -> bool:
        return isinstance(value, BaseObject) and self.id == value.id

    def __hash__(self) -> int:
        return self.id.int

    def destroy(self):
        if self.__destroyed:
            return

        self.scene.remove_object(self)
        self.__destroyed = True
