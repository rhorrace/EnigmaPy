from constants import LETTERS


class Rotor:
    def __init__(self, settings, offset=0):
        self.base = LETTERS
        self.sequence_default = settings[0]
        self.sequence = settings[0]
        self.notches = settings[1]
        self.turnovers = settings[2]
        self.offset = offset
        self.turnover = False

    def forward(self, letter):
        return self.sequence[self.base.index(letter)]

    def reverse(self, letter):
        return self.base[self.sequence.index(letter)]

    def reset(self):
        self.sequence = self.sequence_default
        self.offset = 0

    def ring_setting(self, offset):
        if offset < 0 or offset >= 26:
            raise ValueError("Error: offset must between 0 and 25")

        self.reset()
        self.offset = offset
        self.sequence = self.sequence[self.offset:] + self.sequence[:self.offset]

    def rotate(self):
        self.sequence = self.sequence[1:] + self.sequence[:1]
        self.offset = (self.offset + 1) % 26

        if self.base[self.offset] in self.turnovers:
            self.turnover = True

