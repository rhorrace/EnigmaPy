from constants import LETTERS


class Plugboard:
    def __init__(self, mapping):
        self.plugging = dict(zip(LETTERS, LETTERS))

        for pair in mapping:
            self.plugging[pair[0]] = pair[1]
            self.plugging[pair[1]] = pair[0]

    def forward(self, letter):
        if not letter or letter not in LETTERS:
            raise ValueError(f"Error: character {letter} is not accepted")

        return self.plugging[letter]

    def reverse(self, letter):
        if not letter or letter not in LETTERS:
            raise ValueError(f"Error: character{letter} is not accepted")

        return self.plugging_rev[letter]
