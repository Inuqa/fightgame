from base_scene import BaseScene

class ShowCharactersScene(BaseScene):
    def __init__(self, characters):
        self.characters = characters

    def render(self):
        print(f"""
    Fighters:
    {self.show_fighters()}
        """)

    def show_fighters(self):
        all_fighters = ""
        for f in self.characters:
            all_fighters += str(f)

        return all_fighters
