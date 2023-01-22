import unittest

from constants import LETTERS
from rotor import Rotor


class RotorTest(unittest.TestCase):
    def test_init(self):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        settings = [wiring, "Q", "R"]
        test = Rotor(settings)

        self.__test_rotor(test, wiring)

    def test_forward(self):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        settings = [wiring, "Q", "R"]
        test = Rotor(settings)

        for idx, letter in enumerate(LETTERS):
            self.assertEqual(test.forward(letter), wiring[idx])

    def test_reverse(self):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        settings = [wiring, "Q", "R"]
        test = Rotor(settings)

        for idx, letter in enumerate(wiring):
            self.assertEqual(test.reverse(letter), LETTERS[idx])

    def test_rotate(self):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        test_wiring = "KMFLGDQVZNTOWYHXUSPAIBRCJE"
        settings = [wiring, "Q", "R"]
        test = Rotor(settings)

        test.rotate()

        self.__test_sequence_and_offset(test, wiring, test_wiring, 1)

    def test_rotate_forward(self):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        test_wiring = "KMFLGDQVZNTOWYHXUSPAIBRCJE"
        settings = [wiring, "Q", "R"]
        test = Rotor(settings)

        test.rotate()

        for idx, letter in enumerate(LETTERS):
            self.assertEqual(test.forward(letter), test_wiring[idx])

    def test_rotate_reverse(self):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        test_wiring = "KMFLGDQVZNTOWYHXUSPAIBRCJE"
        settings = [wiring, "Q", "R"]
        test = Rotor(settings)

        test.rotate()

        for idx, letter in enumerate(test_wiring):
            self.assertEqual(test.reverse(letter), LETTERS[idx])

    def test_reset(self):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        settings = [wiring, "Q", "R"]
        test = Rotor(settings)

        test.rotate()
        test.reset()

        self.__test_rotor(test, wiring)

    def test_ring_offset(self):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        test_wiring = "WYHXUSPAIBRCJEKMFLGDQVZNTO"
        settings = [wiring, "Q", "R"]
        test = Rotor(settings)

        self.assertRaises(ValueError, test.ring_setting, -1)
        self.assertRaises(ValueError, test.ring_setting, 26)

        test.ring_setting(13)

        self.__test_sequence_and_offset(test, wiring, test_wiring, 13)

    def __test_rotor(self, rotor, wiring):
        self.assertEqual(rotor.base, LETTERS)
        self.assertEqual(rotor.sequence_default, wiring)
        self.assertEqual(rotor.sequence, wiring)
        self.assertEqual(rotor.notches, "Q")
        self.assertEqual(rotor.turnovers, "R")
        self.assertEqual(rotor.offset, 0)
        self.assertEqual(rotor.turnover, False)

    def __test_sequence_and_offset(self, rotor, wiring, test_wiring, offset):
        self.assertEqual(rotor.sequence_default, wiring)
        self.assertEqual(rotor.sequence, test_wiring)
        self.assertEqual(rotor.offset, offset)

if __name__ == '__main__':
    unittest.main()
