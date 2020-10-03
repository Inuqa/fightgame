from base_scene import BaseScene
from director import Director

class ShowCharacters(BaseScene):
    def render(self):
        print(f"""
        Created Fighters
        
    {self.show_fighters()}
        """)

    def show_fighters(self):
        all_fighters = ""
        for f in Director.characters:
            all_fighters += str(f) + "\n"

        return all_fighters
