from constants import LETTERS, DEFAULT_MAP
from entrywheel import Entrywheel
from rotor import Rotor


class Enigma:
    def __init__(self):
        self.plugboard = {}
        self.entrywheel = Entrywheel()
        self.rotors = []
        self.reflector = {}

    # Since Enigma should self-reciprocate, encoding and decoding is the same
    def encode_decode(self, letter):
        value = letter.upper()

        # Check if letter IS a letter
        if not value.isalpha():
            return value

        # Rotate rotors

        # Go through plugboard

        value = self.plugboard[value]

        # Go through entrywheel

        value = self.entrywheel.forward(value)

        # Go through rotors right-to-left

        # Go through reflector

        value = self.reflector[value]

        # Go through rotors left-to-right

        # Go through entrywheel backwards

        value = self.entrywheel.reverse(value)

        # Go through plugboard

        value = self.plugboard[value]

        return value

    def set_reflector(self, wiring=None):
        if not wiring:
            self.reflector = DEFAULT_MAP
            return

        self.reflector = dict(zip(LETTERS, wiring))

    def set_plugboard(self, mapping=None):
        self.plugboard = DEFAULT_MAP

        if not mapping:
            return

        for pair in mapping:
            self.plugboard[pair[0]] = pair[1]
            self.plugboard[pair[1]] = pair[0]

    def set_rotors(self, rotor_numbers=None):
        if not rotor_numbers:
            rotor_numbers = ["III", "II", "I"]

        if len(rotor_numbers) not in [3,4]:
            rotor_numbers = ["III", "II", "I"]

    def build_rotors(self, rotor_numbers):
        rotors = []
        with open("rotors.csv", "r") as file:
            rotor_details = file.readlines()
            rotor_details = list(map(lambda x: x.strip().split(","), rotor_details))

