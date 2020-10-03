import json

class Fighter:
    FILENAME = 'fighters.json'

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = value

    @staticmethod
    def _load_data():
        try:
            with open(Fighter.FILENAME) as f:
                return json.load(f)
        except FileNotFoundError as e:
            with open(Fighter.FILENAME, 'w') as f:
                json.dump({}, f)
            return {}

    @staticmethod
    def all():
        fighters = []
        for key, value in Fighter._load_data().items():
            fighters.append(
                Fighter(
                    key,
                    value['hp'],
                    value['attack'],
                    value['defense']
                    )
                )
        return fighters

    @staticmethod
    def find(name):
        data = Fighter._load_data()[name]
        return Fighter(
                name,
                data['hp'],
                data['attack'],
                data['defense']
                )

    def serialize(self):
        return {
            'hp': self.hp,
            'attack': self.attack,
            'defense': self.defense,
        }

    def save(self):
        data = Fighter._load_data()
        data[self.name] = self.serialize()
        with open(Fighter.FILENAME, 'w') as f:
            json.dump(data, f)

    def __str__(self):
        return f"""
        Name : {self.name}
          HP : {self.hp}
  Attack DMG : {self.attack}
     Defense : {self.defense}
"""
