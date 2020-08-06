# abstration means hiding of informations or abstracting away information
# give access only what necessary

class PlayerCharacter:

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def speak(self):  # methods
        return f'My name is {self.name}'


player1 = PlayerCharacter('Mishal', 24)

print(player1.speak())
