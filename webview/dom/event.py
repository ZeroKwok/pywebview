import logging
from typing import Any, Callable
# from typing_extensions import Self
from webview import Window
from webview.dom.element import Element

logger = logging.getLogger(__file__)

class DOMEvent:
    def __init__(self, event, window: Window, element: Element) -> None:
        self.event = event
        self.__element = element
        self._items: list = []

    def __add__(self, item):
        self._items.append(item)
        self.__element.on(self.event, item)
        return self
    def __sub__(self, item):
        self._items.remove(item)
        self.__element.off(self.event, item)
        return self

    def __iadd__(self, item):
        self._items.append(item)
        self.__element.on(self.event, item)
        return self

    def __isub__(self, item):
        if item in self._items:
            self._items.remove(item)
            self.__element.off(self.event, item)
        else:
            logger.warning(f'Event handler {item} not found')
        return self
