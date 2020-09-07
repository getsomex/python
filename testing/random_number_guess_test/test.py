import unittest
import script


class TestMain(unittest.TestCase):
    def test_guessTheNumber(self):
        answer = 5
        guess = 5
        result = script.run_guess(answer, guess)
        self.assertTrue(result)

    def test_wrong_guess(self):
        result = script.run_guess(5, 0)
        self.assertFalse(result)

    def test_wrong_number(self):
        result = script.run_guess(5, 11)
        self.assertFalse(result)


if __name__ == '__main__':

    unittest.main()
