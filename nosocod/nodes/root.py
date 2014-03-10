from nosocod.nodes.node import Node


class Root(Node):

    DEFAULT_NAME = 'root'

    DEFAULT_VALUE = ''

    def __init__(self):
        Node.__init__(self, self.DEFAULT_NAME)
        self.value = self.DEFAULT_VALUE

    def is_valid(self, value):
        result = False
        if value == self.value:
            result = True
        return result
