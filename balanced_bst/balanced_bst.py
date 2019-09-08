from lib.ppbtree import ppbtree

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        """ Convenience pointer to assist with rotations """
        self.parent = None

    def __str__(self):
        return str(self.value)

    def __insert_left(self, value):
        if self.left:
            self.left.insert(value)
        else:
            self.set_left(BinaryTreeNode(value))

    def __insert_right(self, value):
        if self.right:
            self.right.insert(value)
        else:
            self.set_right(BinaryTreeNode(value))

    # TODO: handle self-balancing in this function
    def insert(self, value):
        if value <= self.value:
            self.__insert_left(value)
        else:
            self.__insert_right(value)

    def balance(self):
        left_height = 0
        right_height = 0
        if self.left:
            self.left.balance()
            left_height = self.left.height() + 1
        if self.right:
            self.right.balance()
            right_height = self.right.height() + 1
        if left_height - right_height > 1:
            self.left.rotate_right()
        elif right_height - left_height > 1:
            self.right.rotate_left()

    def set_left(self, left_child):
        self.left = left_child
        if left_child:
            left_child.parent = self

    def set_right(self, right_child):
        self.right = right_child
        if right_child:
            right_child.parent = self

    """
    For rotations, we need to ensure that the following three nodes are updated:
    1. self
    2. self.parent
    3. self.parent.parent (if set)

    Their parent pointers and their left/right child pointers must be changed appropriately

    Function treats self node as the pivot
    """
    def rotate_left(self):
        if self.parent:
            self.parent.right = None
            old_parent = self.parent
            if self.parent.parent:
                self.parent.parent.set_left(self)
            else:
                self.parent = None
            self.set_left(old_parent)

    def rotate_right(self):
        if self.parent:
            self.parent.left = None
            old_parent = self.parent
            if self.parent.parent:
                self.parent.parent.set_right(self)
            else:
                self.parent = None
            self.set_right(old_parent)

    def height(self, current_level=0):
        height_left = current_level
        height_right = current_level
        if self.left:
            height_left = self.left.height(current_level + 1)
        if self.right:
            height_right = self.right.height(current_level + 1)
        return max(height_left, height_right)

class BalancedBST:
    def __init__(self, root_val):
        self.root = BinaryTreeNode(root_val)

    # TODO implement this func
    def insert(self, value):
        self.root.insert(value)

    # TODO implement this func
    def remove(self, value):
        pass

    # Util debugging method to fix root pointer
    def update_root(self):
        while (self.root.parent):
            self.root = self.root.parent

    """
    Convenience methods which update the root after performing a rotation on a node
    """

    def rotate_left(self, node):
        node.rotate_left()
        self.update_root()

    def rotate_right(self, node=None):
        node.rotate_right()
        self.update_root()

    """
    Expose this method for manual testing
    """
    def balance(self):
        self.root.balance()
        self.update_root()

    # Return True or False for if tree contains
    # TODO
    def search(self, value):
        pass

    # Returns number (heigh of tree)
    # TODO
    def height(self):
        return self.root.height() + 1

    # Prints a visual representation of tree
    def pretty_print(self):
        ppbtree.print_tree(self.root)
