import unittest
from main import Monomial

class TestMonomial(unittest.TestCase):
    def test_deriv(self):
        self.assertEqual(Monomial.differentiate(Monomial('18')), '0')
        self.assertEqual(Monomial.differentiate(Monomial('x')), '1')
        self.assertEqual(Monomial.differentiate(Monomial('10x')), '10')
        self.assertEqual(Monomial.differentiate(Monomial('5x^5')), '25x^4')
        self.assertEqual(Monomial.differentiate(Monomial('-3x^-3')), '9x^-4')
        self.assertEqual(Monomial.differentiate(Monomial('-3x^-3')), '9x^-4')
        self.assertEqual(Monomial.differentiate(Monomial('x^-2')), '-2x^-3')
        self.assertEqual(Monomial.differentiate(Monomial('5x^-1')), '-5x^-2')
