from constants import LETTERS
from entrywheel import Entrywheel
from plugboard import Plugboard
from reflector import Reflector
from rotor import Rotor


class Enigma:
    def __init__(self):
        default_rotor = [LETTERS, "Z", "A"]
        self.plugboard = Plugboard()
        self.entrywheel = Entrywheel()
        self.rotors = [Rotor(default_rotor, 0)] * 3
        self.reflector = Reflector()
