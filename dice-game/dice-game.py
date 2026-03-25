import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value

class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10



# Testing the class
die = Die()

print(die.value)

die.roll()

print(die.value)