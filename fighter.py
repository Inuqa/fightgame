class Fighter:
    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack_dmg = attack
        self.defence = defence

    def attack(self, b):
        b.hp = (b.hp + b.defence) - self.attack_dmg

    def show_status(self):
        print(self.name, self.hp)
