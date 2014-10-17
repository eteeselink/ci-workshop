import unittest
import cli

class TestParser(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(cli.parse([]), [])
        None
