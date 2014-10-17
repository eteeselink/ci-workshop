import unittest
from visualizer import visualizer

class TestParser(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(visualizer.hello(), "visualizing!")
