import unittest
from calculator import Calculator
from discount import Discount


class TestCalculator(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(Calculator.calculation(2, 6, '+'), 8)

    def test_minus(self):
        self.assertEqual(Calculator.calculation(2, 2, '-'), 0)

    def test_multiply(self):
        self.assertEqual(Calculator.calculation(2, 7, '*'), 14)

    def test_divide(self):
        self.assertEqual(Calculator.calculation(100, 50, '/'), 2)


class TestDiscount(unittest.TestCase):

    def test_discount(self):
        self.assertAlmostEqual(Discount.calculating_discount(100, 5), 95)

    def test_discount_error_1(self):
        """The discount amount cannot be negative!"""
        with self.assertRaises(ValueError):
            Discount.calculating_discount(100, -5)

    def test_discount_error_2(self):
        """The discount amount cannot be more than 100 %!"""
        with self.assertRaises(ValueError):
            Discount.calculating_discount(100, 105)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    