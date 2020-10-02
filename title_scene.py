from base_scene import BaseScene
from event_system import EventSystem

class TitleScene(BaseScene):
    def get_name(self):
        return 'TITLE_SCENE'

    def render(self):
        print("""
        Game
        """)

    def loop(self):
        input()
        EventSystem.emit('DONE', self)
