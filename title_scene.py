from base_scene import BaseScene

class TitleScene(BaseScene):
    def get_name(self):
        return 'TITLE_SCENE'

    def render(self):
        print("""
        Game
        """)
