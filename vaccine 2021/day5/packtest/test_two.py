import unittest

class TestAdd(unittest.TestCase):

	def test_add(self):
		self.assertEqual (sum([6, 4, 3]), 13, "expecting 13") 

	def test_add_two(self):
		self.assertEqual (sum([6, 4, 3]), 16, "expecting 13") 


if __name__ == '__main__':
	unittest.main()

