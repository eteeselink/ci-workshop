import unittest
from extrapolator import extrapolator

class TestParser(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(extrapolator.hello(), "extrapolating!")
