from enum import Enum

from fighter import Fighter
from base_scene import BaseScene
from event_system import EventSystem

class CreateFighterScene(BaseScene):
    class Events(Enum):
        DONE = 2

    def render(self):
        print("""
        Create a Fighter
        """)

    def create(self):
        name = input("Name: ")
        hp = int(input("hp: "))
        attack = int(input("Attack damage: "))
        defence = int(input("Defence: "))

        Fighter.fighter_created.append(Fighter(name, hp, attack, defence))

    def loop(self):
        CreateFighterScene.create(self)
        input()
        EventSystem.emit(CreateFighterScene.Events.DONE, self)
