from constants import LETTERS


class Reflector:
    def __init__(self, letters=LETTERS):
        self.wiring = dict(zip(LETTERS, letters))

    def reflect(self, letter):
        return self.wiring[letter]
