import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) # assert actual output vs. expected output

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(3, -2), 5)

    def test_mult(self):
        self.assertEqual(self.calc.multiply(-2, 2), -4)

    def test_mult_zero(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def test_div(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_div2(self):
        self.assertEqual(self.calc.divide(8, -2), -4)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(8, 2), 0)

    def test_mod2(self):
        self.assertEqual(self.calc.modulo(9, 2), 1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()