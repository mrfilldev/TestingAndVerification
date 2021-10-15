import unittest
from Calculator import calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)  # add assertion here

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()
