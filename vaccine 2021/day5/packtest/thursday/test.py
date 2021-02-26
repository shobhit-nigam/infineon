import unittest

from app import add

class TestAdd(unittest.TestCase):
	def test_seq(self):
		lista = [4, 5, 6]
		result = add(lista)
		self.assertEqual(result, 15)

if __name__ == '__main__':
	unittest.main()


