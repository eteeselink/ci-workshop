import unittest
from logparser import parser

class TestParser(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(parser.hello(), "parsing!")
