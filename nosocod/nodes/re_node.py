from nosocod.nodes.node import Node


class ReNode(Node):

    pattern = None

    def __init__(self, name, pattern):
        Node.__init__(self, name)
        self.pattern = pattern
        self.value = ''

    def is_valid(self, value):
        return self.pattern.match(value)
