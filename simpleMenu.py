import keyboard


class SimpleMenu:
    def __init__(self):
        self.menu_text = """
            Welcome
        """

    def show_menu(self):
        print(self.menu_text)
        while True:
            try:
                if keyboard.is_pressed('q'):
                    break
            except:
                break
