class Node:
    """Binary Search Tree Insertion."""

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:
    """Binary Search Tree."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value to a binary tree."""
        # Check if the value can be inserted to as the root node.
        # In this case the binary tree is the root node.
        # The value can then be added directly to the tree.

        # insert the node as the root node
        if self.root == None:
            self.root = Node(value)

        # call a recursive function to insert the node under the root node.
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        """Recursive function that inserts a node after the current root node."""

        # check if the value is less than then current node
        if value < curr_node.value:
            # check if the current node has a left child.
            # First case is if the current node does not have a left.
            if curr_node.left_child == None:
                # assign the new value to be the current node
                curr_node.left_child = Node(value)
                curr_node.left_child.parent = curr_node
            else:
                # calling the recursive function again with the left child as the current node
                self._insert(value, curr_node.left_child)
        elif value > curr_node.value:
            if curr_node.right_child == None:
                curr_node.right_child = Node(value)
                curr_node.right_child.parent = curr_node
            else:
                self._insert(value, curr_node.right_child)
        else:
            print("Value already in tree")

    def show_tree(self):
        if self.root != None:
            self._show_tree(self.root)

    def _show_tree(self, curr_node):
        if curr_node != None:
            self._show_tree(curr_node.left_child)
            print(str(curr_node.value))
            self._show_tree(curr_node.right_child)

    def tree_height(self):
        if self.root != None:
            return self._tree_height(self.root, 0)
        else:
            return 0

    def _tree_height(self, curr_node, curr_height):
        if curr_node == None:
            return curr_height
        left_height = self._tree_height(curr_node.left_child, curr_height + 1)
        right_height = self._tree_height(
            curr_node.right_child, curr_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        return False

    def _search(self, value, curr_node):
        if value == curr_node.value:
            return True
        elif value < curr_node.value and curr_node.left_child != None:
            # return the recursive search function
            return self._search(value, curr_node.left_child)
        elif value > curr_node.value and curr_node.right_child != None:
            return self._search(value, curr_node.right_child)
        return False

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, curr_node):
        if value == curr_node.value:
            return curr_node
        elif value < curr_node.value and curr_node.left_child != None:
            return self._find(value, curr_node.left_child)
        elif value > curr_node.value and curr_node.right_child != None:
            return self._find(value, curr_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        # Protect against deleting a node not found in the tree
        if node == None or self.find(node.value) == None:
            print("Node to be deleted not found in the tree!")
            return None

        def min_value_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        def num_children(n):
            num_children = 0
            if n.left_child != None:
                num_children += 1
            elif n.right_child != None:
                num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # node has no children
        #  CASE 1
        if node_children == 0:
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # remove the reference to n ide from the parent
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # node has one child
        #  CASE 2
        if node_children == 1:

            # get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child
                # deleted the root node it would delete entire tree.
            if node_parent != None:
                # replace the node to be deleted with it's child node
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = None
            child.parent = node_parent

        # node has two children
        # CASE 3
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete

            node.value = successor.value

            # call the delete node method recursively.
            # delete the successor value now that it's value was copied into the other node
            self.delete_node(successor)


def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        curr_element = randint(0, max_int)
        tree.insert(curr_element)
    return tree


tree = BinarySearchTree()

tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(8)
tree.insert(4)
tree.insert(2)
tree.insert(9)
tree.insert(0)
tree.insert(11)
tree.insert(12)


tree.show_tree()

print(f"current height is: {str(tree.tree_height())}")
print("Found", tree.search(11))
print("Found", tree.search(50))

# tree.delete_value(9)
# tree.delete_value(6)
# tree.delete_value(4)
# tree.delete_value(2)
# tree.delete_value(11)
# tree.delete_value(5)
tree.show_tree()
