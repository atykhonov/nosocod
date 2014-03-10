import unittest2
from nosocod import root


class RootTest(unittest2.TestCase):

    def test_root_name(self):
        self.assertEquals(root.name, 'root')

    def test_root_value(self):
        self.assertEquals(root.value, '')

    def test_is_valid_empty_value(self):
        self.assertTrue(root.is_valid(''))

    def test_is_valid_not_empty_value(self):
        self.assertFalse(root.is_valid('test'))
