class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')


wizard1 = Wizard('Jello', 20)
archer1 = Archer('Kello', 30)


def player_attack(char):
    char.attack()


# player_attack(wizard1)
# player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()
