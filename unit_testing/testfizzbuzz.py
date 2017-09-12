import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_3(self):
        self.assertEqual(fizzbuzz.get_output(3), "Fizz")

    def test_fizz_33(self):
        self.assertEqual(fizzbuzz.get_output(33), "Fizz")

    def test_buzz_5(self):
        self.assertEqual(fizzbuzz.get_output(5), "Buzz")

    def test_buzz_55(self):
        self.assertEqual(fizzbuzz.get_output(55), "Buzz")

    def test_fizzbuzz_15(self):
        self.assertEqual(fizzbuzz.get_output(5), "FizzBuzz")

    def test_fizzbuzz_90(self):
        self.assertEqual(fizzbuzz.get_output(90), "FizzBuzz")

    def test_int_2(self):
        self.assertEqual(fizzbuzz.get_output(2), "2")

    def test_int_11(self):
        self.assertEqual(fizzbuzz.get_output(11), "11")
