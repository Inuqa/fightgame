from event_system import EventSystem

from title_scene import TitleScene
from menu_scene import MenuScene
from create_character_scene import CreateFighterScene
from show_characters import ShowCharacters


class Director:
    current_scene = None
    characters = []

    def __init__(self):
        EventSystem.subscribe(self)

    def receive(self, message, emitter=None, data=None):
        if message == TitleScene.Events.DONE:
            current_scene = MenuScene()
            current_scene.render()
            current_scene.loop()
        elif message == MenuScene.Events.CREATE_CHARACTER:
            current_scene = CreateFighterScene()
            current_scene.render()
            current_scene.loop()
        elif message == CreateFighterScene.Events.CREATE:
            Director.characters.append(data)

        elif message == CreateFighterScene.Events.DONE:
            current_scene = MenuScene()
            current_scene.render()
            current_scene.loop()

        elif message == MenuScene.Events.LIST_CHARACTER:
            current_scene = ShowCharacters(self.characters)
            current_scene.render()
            current_scene.show_fighters()

        elif message == MenuScene.Events.SELECT_CHARACTER:
            # TODO:
            print('PENDING: make select character scene')
        elif message == MenuScene.Events.REMOVE_CHARACTER:
            # TODO:
            print('PENDING: make remove character scene')

    def start(self):
        current_scene = TitleScene()
        current_scene.render()
        current_scene.loop()
