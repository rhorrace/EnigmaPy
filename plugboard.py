from constants import LETTERS, DEFAULT_MAP


class Plugboard:
    def __init__(self, mapping):
        self.plugging = DEFAULT_MAP

        for pair in mapping:
            self.plugging[pair[0]] = pair[1]
            self.plugging[pair[1]] = pair[0]

    def convert(self, letter):
        return self.plugging[letter]
