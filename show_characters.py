from base_scene import BaseScene
from fighter import Fighter

class ShowCharacters(BaseScene):
    def render(self):
        print(f"""
        Created Fighters
        
    {self.show_fighters()}
        """)

    def show_fighters(self):
        all_fighters = ""
        for f in Fighter.fighter_created:
            all_fighters += str(f) + "\n"

        return all_fighters
