from base_scene import BaseScene

class ShowCharacters(BaseScene):
    def __init__(self, characters):
        self.characters = characters

    def render(self):
        print(f"""
        Created Fighters

    {self.show_fighters()}
        """)

    def show_fighters(self):
        all_fighters = ""
        for f in self.characters:
            all_fighters += str(f) + "\n"

        return all_fighters
