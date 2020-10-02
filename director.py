from event_system import EventSystem

from title_scene import TitleScene
from menu_scene import MenuScene

class Director:
    current_scene = None

    def __init__(self):
        EventSystem.subscribe(self)

    def receive(self, message, emitter = None, data = None):
        if message == TitleScene.Events.DONE:
            current_scene = MenuScene()
            current_scene.render()
            current_scene.loop()
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
