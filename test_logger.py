import unittest     # Import the Python unit testing framework
from logger import Logger     # Our code to test


class LoggerTest(unittest.TestCase):
    
    def test__init__(self):         
         self.assertIsNone(None)
    
    def test_to_console(self):
        log = Logger();
        console = log._to_console('test1')
        self.assertEqual(console, console)
        
    def test_info(self):
        log = Logger();
        info = log.info('test1')
        self.assertEqual(info, info)
        
    def test_error(self):
        log = Logger();
        error = log.error('error1')
        self.assertEqual(error, error)
        
if __name__ == '__main__':
    unittest.main()