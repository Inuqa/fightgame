from title_scene import TitleScene
from event_system import EventSystem

class Director:
    current_scene = None

    def __init__(self):
        EventSystem.subscribe(self)

    def receive(self, message, emitter = None, data = None):
        if(message == TitleScene.Events.DONE):
            print('director detected title scene is done...')

    def start(self):
        current_scene = TitleScene()
        current_scene.render()
        current_scene.loop()
