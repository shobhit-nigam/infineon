# unittest skip
# conditinal skipping
import unittest

class TestAdd(unittest.TestCase):
	data = 20
	datb = 30

	def test_add(self):
		self.assertEqual (sum([6, 4, 3]), 13, "expecting 13") 
	
	@unittest.skip("will be tested later")
	def test_add_two(self):
		self.assertEqual (sum([6, 4, 3]), 16, "expecting 13") 
	
	def test_add_three(self):
		self.assertEqual (sum([6, 4, 3]), 16, "expecting 13") 
	
	@unittest.skipIf(datb>data, "skip if")
	def test_add_four(self):
		self.assertEqual (sum([6, 4, 3]), 16, "expecting 13") 

	@unittest.expectedFailure
	def test_add_five(self):
		self.assertEqual (sum([6, 4, 3]), 16, "expecting 13") 

if __name__ == '__main__':
	unittest.main()

