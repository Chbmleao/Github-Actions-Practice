import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calc = Calculator()

  def test_add(self):
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)
    self.assertEqual(self.calc.add(-1, -1), -2)

  def test_subtract(self):
    self.assertEqual(self.calc.subtract(10, 5), 5)
    self.assertEqual(self.calc.subtract(-1, -1), 0)
    self.assertEqual(self.calc.subtract(-1, 1), -2)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(3, 7), 21)
    self.assertEqual(self.calc.multiply(-1, 1), -1)
    self.assertEqual(self.calc.multiply(-1, -1), 1)

  def test_divide(self):
    self.assertEqual(self.calc.divide(10, 2), 5)
    self.assertEqual(self.calc.divide(-1, 1), -1)
    self.assertEqual(self.calc.divide(-1, -1), 1)
    
  def test_divide_by_zero(self):
    with self.assertRaises(ValueError):
      self.calc.divide(10, 0)
    
  def test_power(self):
    self.assertEqual(self.calc.power(2, 3), 8)
    self.assertEqual(self.calc.power(2, 0), 1)
    self.assertEqual(self.calc.power(0, 0), 1)

  def test_negative_power(self):
    self.assertEqual(self.calc.power(2, -3), 1/8)

  def test_factorial(self):
    self.assertEqual(self.calc.factorial(5), 120)
    self.assertEqual(self.calc.factorial(0), 1)
    self.assertEqual(self.calc.factorial(1), 1)

  def test_fibonacci(self):
    self.assertEqual(self.calc.fibonacci(5), 5)
    self.assertEqual(self.calc.fibonacci(0), 0)
    self.assertEqual(self.calc.fibonacci(1), 1)

  def test_is_prime(self):
    self.assertTrue(self.calc.is_prime(2))
    self.assertTrue(self.calc.is_prime(3))
    self.assertTrue(self.calc.is_prime(5))
    self.assertTrue(self.calc.is_prime(7))
    self.assertTrue(self.calc.is_prime(11))
    self.assertFalse(self.calc.is_prime(1))
    self.assertFalse(self.calc.is_prime(4))
    self.assertFalse(self.calc.is_prime(6))
    self.assertFalse(self.calc.is_prime(8))
    self.assertFalse(self.calc.is_prime(9))
    self.assertFalse(self.calc.is_prime(10))

if __name__ == '__main__':
    unittest.main()
