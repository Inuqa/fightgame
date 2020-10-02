from title_scene import TitleScene

class Director:
    current_scene = None

    def receive(self, message, emitter = None, data = None):
        pass

    def start(self):
        current_scene = TitleScene()
        current_scene.render()
        current_scene.loop()
