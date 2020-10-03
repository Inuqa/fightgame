class Fighter:
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

    def __str__(self):
        return f"""
    Name: {self.name}
    HP: {self.hp} 
    Attack DMG {self.attack}
    Defence {self.defence}"""
