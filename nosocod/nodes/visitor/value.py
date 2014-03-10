from nosocod.nodes.visitor.base import Base as Visitor


class Value(Visitor):

    def __init__(self, query):
        Visitor.__init__(self, query)
        self.level = 0

    def _is_valid_node(self, node, value):
        return node.is_valid(value)
