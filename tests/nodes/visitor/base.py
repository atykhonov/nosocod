import unittest2
from nosocod.nodes.visitor.base import Base as Visitor
from nosocod.query.base import Base as Query


class BaseTest(unittest2.TestCase):

    def init_visitor(self, squery):
        return Visitor(Query(squery))

    def test_test(self):
        visitor = self.init_visitor('/test/query')
