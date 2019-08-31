import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        result = maths.add(1,1)
        self.assertEqual(result, 2)

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        fibresult = maths.fibonacci(5)
        self.assertEqual(fibresult, 5)

    def test_convert_base(self):
        baseresult = maths.convert_base(5,3)
        self.assertEqual(baseresult, '12')

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
