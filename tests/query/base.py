from satvika.query.base import Base as Query
from satvika.nodes.node import Node
import unittest


class QueryTest(unittest.TestCase):

    def test_get_chunks(self):
        query_parts = ['test', 'get', 'chunks']
        query = Query(Query.DELIMITER.join(query_parts))
        self.assertEquals(query.get_chunks(), query_parts)

    def test_build_query(self):
        nodes = Node('test'), Node('get'), Node('chunks')
        query = Query.build_query(nodes)
        self.assertEquals(query.query, '/test/get/chunks')
