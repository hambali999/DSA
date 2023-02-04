import unittest

def square(n):
    return n*n

class Test(unittest.TestCase):
    def test_two(self):
        self.assertEqual(square(2), 4)

if __name__=='__main__':
	unittest.main()

