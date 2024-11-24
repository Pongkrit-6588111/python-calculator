import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(1, 3), 4)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)
        self.assertEqual(self.calc.subtract(8, 3), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 9), 9)
        self.assertEqual(self.calc.multiply(12, 12), 144)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(12, 13), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)
        self.assertEqual(self.calc.modulo(10, 11), 10)

    # Add the following test methods to the TestCalculator class:
if __name__ == '__main__':
    unittest.main()