from enum import Enum

from base_scene import BaseScene
from event_system import EventSystem


class MenuScene(BaseScene):
    class Events(Enum):
        CREATE_CHARACTER = 1
        SELECT_CHARACTER = 2
        LIST_CHARACTER = 3
        SELECT_ENEMY_CHARACTER = 4
        REMOVE_CHARACTER = 5

    def render(self):
        print("""
Main Menu:

1) create character
2) select character
3) list characters
4) select enemy (optional)
5) remove character

        """)

    def loop(self):
        option = input('Select option: ')
        event = None
        if option == '1':
            event = MenuScene.Events.CREATE_CHARACTER
        elif option == '2':
            event = MenuScene.Events.SELECT_CHARACTER
        elif option == '3':
            event = MenuScene.Events.LIST_CHARACTER
        elif option == '4':
            event = MenuScene.Events.SELECT_ENEMY_CHARACTER
        elif option == '5':
            event = MenuScene.Events.REMOVE_CHARACTER

        EventSystem.emit(event, self)
