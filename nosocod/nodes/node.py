class Node(object):

    name = ''

    value = ''

    actions = []

    children = []

    parent = None

    params = []

    linked_with = None

    anchored = False

    def __init__(self, name, value=None):
        self.name = name
        # TODO do we realy need this if?
        if value:
            self.value = value
        else:
            # something is wrong with that value assigning
            self.value = name
        self.children = []
        self.params = []
        self.actions = []

    def assign_action(self, action):
        action.set_node(self)
        self.append(action)

    def add_node(self, node):
        self.children.append(node)
        node.parent = self

    def get_children(self):
        result = self.children
        if self.linked_with is not None:
            result = self.linked_with.get_children()
        return result

    def has_children(self):
        return len(self.children) > 0

    def add_param(self, param):
        self.params.append(param)

    def has_params(self):
        return len(self.params) > 0

    def get_param(self, name):
        result = None
        for param in self.params:
            if param.name == name:
                result = param
                break
        return result

    def accept(self, visitor):
        if visitor.visitEnter(self):
            for child in self.children:
                if child.accept(visitor):
                    break
        return visitor.visitLeave(self)

    def is_linked(self):
        return self.linked_with is not None

    def __add__(self, other):
        if isinstance(other, (list, tuple)):
            self.children.extend(other)
        else:
            self.children.append(other)
        return self

    def __sub__(self, other):
        for child in self.children:
            if child.name == other.name:
                self.children.remove(child)
        return self

    def is_valid(self, value):
        result = False
        if self.value == value:
            result = True
        return result

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

"""
    def get_path(self, with_root=True):
        parents = []
        parent = self.parent
        while parent != None:
            parents.append(parent)
            parent = parent.parent

        parents.sort(reverse=True)

        path = ''

        for parent in parents:
            if not with_root and parent.name == 'root':
                continue
            path += '/' + parent.name

        path += '/' + self.name

        return path

    def get_relative_path(self, path):
        # TODO
        pass
"""
