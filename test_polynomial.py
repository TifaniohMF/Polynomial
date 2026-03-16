import unittest
from polynomial import Polynomial

class testPolynomial(unittest.TestCase):
    def test_evaluate(self):
        p = Polynomial([1,2])
        self.assertEqual(p.P(1), 5)
    def addition(self):
        p1 = Polynomial([1,1])
        p2 = Polynomial([2,3])
        p_sum = p1 + p2
        self.assertEqual(p_sum.coeff, [3,4])

if __name__ == '__main__':
    unittest.main()