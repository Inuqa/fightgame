import keyboard


class MainMenu:
    def __init__(self):
        self.menu_text = """
            Fight Menu
    1.- Create a new fighter
    2.- Select a fighter
    3.- Select a enemy
    4.- Start fight        
        """

    def show_menu(self):
        print(self.menu_text)
        while True:
            try:
                if keyboard.is_pressed('1'):
                    create_fighter()
                elif keyboard.is_pressed('2'):
                    

            except:
                break
