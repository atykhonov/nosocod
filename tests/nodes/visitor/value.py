import unittest2
import re
from nosocod.nodes.node import Node
from nosocod.nodes.re_node import ReNode
from nosocod.nodes.root import Root
from nosocod.nodes.visitor.value import Value as Visitor
from nosocod.query.base import Base as Query


# TODO : revamp so this TestCase will contain tests related directly to Visitor
# but not to particular Node
class ValueTest(unittest2.TestCase):

    root_node = None

    test_node = None

    query_node = None

    def init_visitor(self, squery):
        return Visitor(Query(squery))

    def init_simple_node_tree(self):
        self.root_node = Root()
        self.test_node = Node('test')
        self.query_node = Node('query')
        self.test_node += self.query_node
        self.root_node += self.test_node
        return self.root_node

    def init_complex_node_tree(self):
        root = Root()
        root += [Node('about'),
                 Node('contact-us'),
                 Node('products'),
                 Node('product') + ReNode('id', re.compile('\d'))]
        return root

    def test_simple_path(self):
        visitor = self.init_visitor('/test/query')
        root = self.init_simple_node_tree()
        root.accept(visitor)

        for result, expected in zip(visitor.chains, [self.root_node, self.test_node,
                                                     self.query_node]):
            self.assertEquals(result.name, expected.name)

    def test_not_short_existing_path(self):
        visitor = self.init_visitor('/test/not_existing')
        root = self.init_simple_node_tree()
        try:
            root.accept(visitor)
        except Exception:
            pass
        self.assertEquals(len(visitor.chains), 0)

    def test_not_long_existing_path(self):
        visitor = self.init_visitor('/test/query/extra')
        root = self.init_simple_node_tree()

        try:
            root.accept(visitor)
        except Exception:
            pass

        self.assertFalse(visitor.chains)

    def test_with_additional_node(self):
        visitor = self.init_visitor('/test/query')
        root = self.init_simple_node_tree()
        test2_node = Node('test')
        root += test2_node
        root.accept(visitor)

        for result, expected in zip(visitor.chains, [self.root_node, self.test_node,
                                                     self.query_node]):
            self.assertEquals(result.name, expected.name)

        
        # self.assertEquals(visitor.chains[0], [self.root_node, self.test_node,
        #                                       self.query_node])
        # self.assertEquals(visitor.chains[1], [self.root_node, test2_node])

    def test_base_and_re_nodes(self):
        visitor = self.init_visitor('/test/query')
        root = Root()
        test_node = Node('test')
        re_node = ReNode('query', re.compile('[a-z]+'))
        root += test_node + re_node
        root.accept(visitor)

        for result, expected in zip(visitor.chains,
                                    [root, test_node, re_node]):
            self.assertEquals(result.name, expected.name)



if __name__ == '__main__':
    unittest.main()
