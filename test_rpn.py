import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		self.assertEqual(rpn.calculate("1 1 +"), 2)
		self.assertEqual(rpn.calculate("-1.5 0 +"), -1.5)