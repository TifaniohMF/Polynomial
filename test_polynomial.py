import unittest
from polynomial import Polynomial

class TestPolynomial(unittest.TestCase):
    def test_evaluate(self):
        p = Polynomial([1, 2])  # 1 + 2X
        self.assertEqual(p.P(1), 3)
        self.assertEqual(p.P(0), 1)
        self.assertEqual(p.P(2), 5)
    
    def test_addition(self):
        p1 = Polynomial([1, 1])  # 1 + X
        p2 = Polynomial([2, 3])  # 2 + 3X
        p_sum = p1 + p2
        self.assertEqual(p_sum.coeff, [3, 4])  # 3 + 4X
    
    def test_str(self):
        p = Polynomial([1, 2, 3])  # 1 + 2X + 3X^2
        self.assertEqual(str(p), "3X^2 + 2X + 1")
        p2 = Polynomial([0, 1, -1])  # X - X^2
        self.assertEqual(str(p2), "-X^2 + X")
        p3 = Polynomial([0])  # 0
        self.assertEqual(str(p3), "0")
    
    def test_multiplication(self):
        p1 = Polynomial([1, 1])  # 1 + X
        p2 = Polynomial([1, 1])  # 1 + X
        p_prod = p1 * p2
        self.assertEqual(p_prod.coeff, [1, 2, 1])  # 1 + 2X + X^2
    
    def test_subtraction(self):
        p1 = Polynomial([3, 4])  # 3 + 4X
        p2 = Polynomial([1, 1])  # 1 + X
        p_diff = p1 - p2
        self.assertEqual(p_diff.coeff, [2, 3])  # 2 + 3X
    
    def test_equality(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        p3 = Polynomial([1, 2, 4])
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)
    
    def test_degree(self):
        p = Polynomial([1, 2, 3])  # degree 2
        self.assertEqual(p.degree(), 2)
        p_zero = Polynomial([0])
        self.assertEqual(p_zero.degree(), -1)
    
    def test_derivative(self):
        p = Polynomial([1, 2, 3])  # 1 + 2X + 3X^2, derivative: 2 + 6X
        p_deriv = p.derivative()
        self.assertEqual(p_deriv.coeff, [2, 6])
        p_const = Polynomial([5])  # constant, derivative: 0
        self.assertEqual(p_const.derivative().coeff, [0])
    
    def test_scalar_operations(self):
        p = Polynomial([1, 2])  # 1 + 2X
        p_add = p + 3  # 4 + 2X
        self.assertEqual(p_add.coeff, [4, 2])
        p_mul = p * 2  # 2 + 4X
        self.assertEqual(p_mul.coeff, [2, 4])
        p_sub = p - 1  # 0 + 2X
        self.assertEqual(p_sub.coeff, [0, 2])
        # Reverse operations
        p_radd = 3 + p
        self.assertEqual(p_radd.coeff, [4, 2])
        p_rmul = 2 * p
        self.assertEqual(p_rmul.coeff, [2, 4])