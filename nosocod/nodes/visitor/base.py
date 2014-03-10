import copy
from nosocod.nodes.node import Node


class Base(object):

    chain = []

    chains = []

    query = None

    locked = False

    level = 0

    valid_node = False

    def __init__(self, query):
        self.query = query
        self.chain = []
        self.chains = []

    # rename to visit_enter
    def visitEnter(self, node):
        result = False
        self.valid_node = False

        value = self._get_value_from_query()

        if self._is_valid_node(node, value):
            if not self._is_locked(node):

                self.valid_node = True

                newnode = Node(node.name)
                newnode.value = value
                self.chains.append(newnode)

                if node.is_linked():
                    self.locked[node.get_path()] = node.get_path()

                result = True

        self.level += 1

        return result

    # rename to visit_leave
    def visitLeave(self, node):
        if self._is_locked(node):
            self._unlock(node)
        if not self.valid_node:
            self.chains = []
            raise Exception('Not found.')
        # if (not node.anchored
        #     and (len(self.query.get_chunks()) - 1) == self.level):
        #     self.chains = []
        #     raise Exception('Not found.')
        if (self.valid_node
             and not node.children
             and len(self.query.get_chunks()) > self.level):
            self.chains = []
            raise Exception('Not found.')
           
        self.level -= 1
        # if self.valid_node:
        #     if not node.has_children():
        #         self.chains.append(copy.deepcopy(self.chain))
        #     newnode = Node(node.name)
        #     self.chain -= newnode

    def _is_locked(self, node):
        result = False
        if node.is_linked():
            if node.getPath() in self.locked:
                result = True
        return result

    def _unlock(self, node):
        self.locked[node.get_path()] = None

    def _get_value_from_query(self):
        result = None

        parts = self.query.get_chunks()

        return parts[self.level]

    def _is_valid_node(self):
        # abstract method
        pass
