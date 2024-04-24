from pygame import Surface, Event


class BaseObject:
    def update(self, delta: float):
        pass

    def draw(self, screen: Surface):
        pass

    def handle_event(self, event: Event):
        pass