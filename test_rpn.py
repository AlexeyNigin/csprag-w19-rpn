import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_invalid(self):
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "wazzup")
	def test_add(self):
		self.assertEqual(rpn.calculate("1 1 +"), 2)
		self.assertEqual(rpn.calculate("-1.5 0 +"), -1.5)
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "1 +")
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "+")
	def test_subtract(self):
		self.assertEqual(rpn.calculate("2 1 -"), 1)
		self.assertEqual(rpn.calculate("0 -1.5 -"), 1.5)
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "1 -")
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "-")
	def test_multiply(self):
		self.assertEqual(rpn.calculate("2 2 *"), 4)
		self.assertEqual(rpn.calculate("0 0 *"), 0)
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "1 *")
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "*")
	def test_divide(self):
		self.assertEqual(rpn.calculate("4 2 /"), 2)
		self.assertEqual(rpn.calculate("0 5 /"), 0)
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "1 0 /")
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "1 /")
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "/")
	def test_nest(self):
		self.assertEqual(rpn.calculate("6 2 2 + 4 1 - * + 2 /"), 9)
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "1 1")
		self.assertRaises(rpn.CalculatorError, rpn.calculate, "1 1 + +")