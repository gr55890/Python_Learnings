import unittest

def isEven(n):
    if (n%2)==0:
        return True
    else:
        return False

class TestIsEvenMethod(unittest.TestCase):
    def test_isEven1(self):
        result=isEven(5)	
        self.assertEqual(result,False)

    def test_isEven2(self):
        result=isEven(10)
        self.assertEqual(result,True)

    def test_isEven3(self):
        self.assertRaises(TypeError,isEven,'hello')

if __name__ == '__main__':
	unittest.main()