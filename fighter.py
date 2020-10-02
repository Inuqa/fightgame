class Fighter:
    fighter_created = []

    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def modify(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def show_stats(self):
        print(self.name, self.hp, self.attack, self.defence)
