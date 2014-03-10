import unittest2
import re
from nosocod.nodes.re_node import ReNode


class ReNodeTest(unittest2.TestCase):

    def init_re_node(self):
        self.name = 'surname'
        self.pattern = re.compile('[a-z]+')
        return ReNode(self.name, self.pattern)

    def test_init(self):
        re_node = self.init_re_node()
        self.assertEquals(re_node.name, self.name)
        self.assertEquals(re_node.pattern, self.pattern)
        self.assertFalse(re_node.value)

    def test_is_valid_false(self):
        re_node = self.init_re_node()
        self.assertFalse(re_node.is_valid("202020"))

    def test_is_valid_true(self):
        re_node = self.init_re_node()
        self.assertTrue(re_node.is_valid("thetest"))
