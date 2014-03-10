import unittest2
from mock import Mock
from nosocod.nodes.node import Node


class NodeTest(unittest2.TestCase):

    def init(self, name, value=None):
        return Node(name, value)

    def init_default(self):
        return Node('name', 'value')

    def init_parent_child(self):
        return Node('parent'), Node('child')

    def test_init_name(self):
        node = self.init('name')
        self.assertEquals(node.name, 'name')

    def test_init_empty_value(self):
        node = self.init('name', '')
        self.assertEquals(node.value, node.name)

    def test_init_not_empty_value(self):
        node = self.init('name', 'value')
        self.assertEquals(node.value, 'value')

    def test_add_node_children(self):
        parent, child = self.init_parent_child()
        parent.add_node(child)
        self.assertEquals(parent.children, [child])

    def test_add_node_parent(self):
        parent, child = self.init_parent_child()
        parent.add_node(child)
        self.assertEquals(child.parent, parent)

    def test_get_children_without_linked(self):
        parent, child = self.init_parent_child()
        parent.add_node(child)
        self.assertEquals(parent.children, [child])

    def test_get_children_with_linked(self):
        parent, child = self.init_parent_child()
        parent.add_node(child)

        root = self.init('root')
        linked = self.init('linked')
        root.linked_with = parent

        self.assertEquals(root.get_children(), [child])

    def test_has_children_empty(self):
        parent, child = self.init_parent_child()
        self.assertFalse(parent.has_children())

    def test_has_children_not_empty(self):
        parent, child = self.init_parent_child()
        parent.add_node(child)
        self.assertTrue(parent.has_children())

    def test_add_param(self):
        node = self.init_default()
        node.add_param('param')
        self.assertEquals(node.params, ['param'])

    def test_has_params_empty(self):
        node = self.init_default()
        self.assertFalse(node.has_params())

    def test_has_params_not_empty(self):
        node = self.init_default()
        node.add_param('param')
        self.assertTrue(node.has_params())

    def test_accept_visitor_enter(self):
        node = self.init_default()
        visitor = Mock(name='visitor')
        node.accept(visitor)
        visitor.visitEnter.assert_called_with(node)

    def test_accept_visitor_leave(self):
        node = self.init_default()
        visitor = Mock(name='visitor')
        node.accept(visitor)
        visitor.visitLeave.assert_called_with(node)

    def test_accept_visitor_accept_child(self):
        parent, child = self.init_parent_child()
        parent.add_node(child)
        visitor = Mock(name='visitor')
        visitor.visitEnter.return_value = True
        child.accept = Mock(name='accept')
        parent.accept(visitor)
        child.accept.assert_called_with(visitor)

    def test_is_linked_true(self):
        parent, child = self.init_parent_child()
        parent.linked_with = child
        self.assertTrue(parent.is_linked())

    def test_is_linked_false(self):
        node = self.init_default()
        self.assertFalse(node.is_linked())

    def test_add_single(self):
        parent, child = self.init_parent_child()
        parent += child
        self.assertEquals(parent.children, [child])

    def test_add_list(self):
        parent, child = self.init_parent_child()
        child2 = self.init_default()
        children = [child, child2]
        parent += children
        self.assertEquals(parent.children, children)

    def test_add_tuple(self):
        parent, child = self.init_parent_child()
        child2 = self.init_default()
        children = (child, child2)
        parent += children
        self.assertEquals(parent.children, [child, child2])

    def test_sub_node(self):
        parent, child = self.init_parent_child()
        parent += child
        parent -= child
        self.assertEquals(parent.children, [])

    def test_to_string(self):
        node = Node('name')
        self.assertEquals(node.name, str(node))

    def test_to_unicode(self):
        node = Node('name')
        self.assertEquals(node.name, unicode(node))
