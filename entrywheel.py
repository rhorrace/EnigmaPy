from constants import LETTERS


class Entrywheel:
    def __init__(self, letters=LETTERS):
        self.wiring = dict(zip(LETTERS, letters))
        self.wiring_rev = dict(zip(letters, LETTERS))

    def forward(self, letter):
        if not letter or letter not in LETTERS:
            raise ValueError(f"Error: character {letter} is not accepted")

        return self.wiring[letter]

    def reverse(self, letter):
        if not letter or letter not in LETTERS:
            raise ValueError(f"Error: character{letter} is not accepted")

        return self.wiring_rev[letter]
