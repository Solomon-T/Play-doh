import unittest
import main

class TestMain(unittest.TestCase):
    def test_fn(self):
        test_param = 10
        result = main.fn(test_param)
        self.assertEqual(result, 15)

unittest.main() # So this has nothing to do with the name of the main file