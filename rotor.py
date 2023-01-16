class Rotor:
    def __init__(self):
        self.wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.turnover = ""
        self.position = 0

    def set_wiring(self, setting):
        if not setting:
            return

        if len(setting) != 26 or not setting.isalpha():
            return

        self.wiring = setting.upper()

    def set_turnover(self, letter):
        self.turnover = letter

    def rotate(self):
        self.wiring = self.wiring[-1] + self.writing[:-1]
        self.position = (self.position + 1) % 26
