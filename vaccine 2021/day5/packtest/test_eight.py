# unittest skip
# conditinal skipping
import unittest

def divide(la, lb):
	return la/lb

class TestAdd(unittest.TestCase):

	def setUp(self):
		self.data = 10
		self.datb = 30

	def test_add(self):
		print("data =", self.data)
		self.assertEqual (divide(self.datb, self.data), 3.0)
		
	def teraDown(self):
		self.data = 100
		self.datb = 300


if __name__ == '__main__':
	unittest.main()

