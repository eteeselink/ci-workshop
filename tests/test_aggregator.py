import unittest
from aggregator import aggregator

class TestParser(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(aggregator.hello(), "aggregating!")
