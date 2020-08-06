class PlayerCharacter:
    membership = True  # Class Object attribute

    def __init__(self, name, age):
        if(self.membership):
            self.name = name  # attributes
            self.age = age

    def shout(self):  # methods
        return f'My name is {self.name}'


player1 = PlayerCharacter('Mishal', 24)
player2 = PlayerCharacter('Fahim', 12)
print(player1.shout())
print(player2.shout())
print(player1.membership)
