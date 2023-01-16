import re

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def set_settings(setting):
    default = {letter: letter for letter in LETTERS}

    if not setting:
        return default
    if len(setting) != 26 or not setting.isalpha():
        return default

    return {letter1: letter2 for letter1, letter2 in zip(LETTERS, setting)}


class Enigma:
    def __init__(self):
        self.plugboard = {}
        self.entrywheel = {}
        self.rotors = []
        self.reflector = {}

    def set_plugboard(self, settings=None):
        self.plugboard = {letter: letter for letter in LETTERS}

        if not settings:
            return

        settings = settings.upper()
        pairs = settings.split()

        if any(lambda p: len(p) != 2 and p.isalpha(), pairs) or len(pairs) > 20:
            return

        for pair in pairs:
            x, y = pair[0], pair[1]
            self.plugboard[x] = y
            self.plugboard[y] = x

    def set_entrywheel(self, setting):
        self.entrywheel = set_settings(setting)

    def set_reflector(self, setting):
        self.reflector = set_settings(setting)

