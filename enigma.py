from constants import LETTERS, DEFAULT_MAP
from entrywheel import Entrywheel
from rotor import Rotor


class Enigma:
    def __init__(self):
        self.plugboard = {}
        self.entrywheel = Entrywheel()
        self.rotors = []
        self.reflector = {}

        self.build_rotors(["III", "II", "I"])

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

        for rotor in reversed(self.rotors):
            value = rotor.forward(value)

        # Go through reflector

        value = self.reflector[value]

        # Go through rotors left-to-right

        for rotor in self.rotors:
            value = rotor.reverse(value)

        # Go through entrywheel backwards

        value = self.entrywheel.reverse(value)

        # Go through plugboard

        value = self.plugboard[value]

        return value

    def set_reflector(self, letter=None):
        if letter is None:
            self.reflector = DEFAULT_MAP

    def build_reflector(self, letter):
        pass

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

        if len(rotor_numbers) not in [3, 4]:
            rotor_numbers = ["III", "II", "I"]

        self.build_rotors(rotor_numbers)

    def build_rotors(self, rotor_numbers):
        rotors = [None] * len(rotor_numbers)
        rotor_details = []

        with open("rotors.csv", "r") as file:
            rotor_details = file.readlines()

        if not rotor_details:
            raise Exception("Failed to retrieve rotor data.")

        rotor_details = list(map(lambda x: x.strip().split(","), rotor_details))

        for rotor in rotor_details:
            if rotor[0] not in rotor_numbers:
                continue

            idx = rotor_numbers.index(rotor[0])
            rotors[idx] = Rotor(rotor[1:])

        self.rotors = rotors
