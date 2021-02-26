# unittest skip
# conditinal skipping
import unittest

def divide(la, lb):
	return la/lb

class TestAdd(unittest.TestCase):
	data = 10
	datb = 30

	def test_add(self):
		self.assertRaises (ZeroDivisionError,  divide, self.datb, self.data)
	"test fails if exception is not raised"
	"test passes if ZeroDivisionError is raised"	


'''	
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
'''

if __name__ == '__main__':
	unittest.main()

