from satvika.nodes.visitor.base import Base as Visitor


class Path(Visitor):

    def __init__(self, query):
        Visitor.__init__(query)
        self.level = 1

    def _is_valid_node(self, node, value):
        return node.name == value
