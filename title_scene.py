from enum import Enum

from base_scene import BaseScene
from event_system import EventSystem

class TitleScene(BaseScene):
    class Events(Enum):
        DONE = 1

    def render(self):
        print("""
        Game
        """)

    def loop(self):
        input()
        EventSystem.emit(TitleScene.Events.DONE, self)
