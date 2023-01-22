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

    def forward(self, index):
        return self.base.index(self.sequence[index])

    def reverse(self, index):
        return self.sequence.index(self.base[index])

    def reset(self):
        self.base = LETTERS
        self.sequence = self.sequence_default
        self.offset = 0

    def ring_setting(self):
        self.base = self.base[self.offset:] + self.base[:self.offset]
        self.sequence = self.sequence[self.offset:] + self.sequence[:self.offset]

    def rotate(self):
        self.base = self.base[1:] + self.base[:1]
        self.sequence = self.sequence[1:] + self.sequence[:1]
        self.offset = (self.offset + 1) % 26

        if self.base[0] in self.turnovers:
            self.turnover = True

