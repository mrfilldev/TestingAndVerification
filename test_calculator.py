import unittest
import Calculator


class TestCalculator(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.calculator = Calculator()

    # Each test method starts with the keyword test_
    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 6)

    if __name__ == "__main__":
        unittest.main()
