import unittest

from funkce import fizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_simple_three(self):
        assert fizzBuzz(3) == "Fizz"

    def test_fizz_simple_five(self):
        assert fizzBuzz(5) == "Buzz"

    def test_fizz_simple_combined(self):
        assert fizzBuzz(15) == "FizzBuzz"
