from constants import LETTERS


class Entrywheel:
    def __init__(self, letters=LETTERS):
        self.wiring = dict(zip(LETTERS, letters))
        self.wiring_rev = dict(zip(letters, LETTERS))

    def forward(self, letter):
        return self.wiring[letter]

    def reverse(self, letter):
        return self.wiring_rev[letter]
