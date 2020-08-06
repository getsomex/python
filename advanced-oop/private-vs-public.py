# for convention python programmers use _ to denote a private variable or methods
class PlayerCharacter:

    def __init__(self, name, age):
        self._name = name  # attributes
        self._age = age

    def _speak(self):  # methods
        return f'My name is {self._name}'


player1 = PlayerCharacter('Mishal', 24)

print(player1._speak())
