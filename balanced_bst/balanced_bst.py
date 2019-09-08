from lib.ppbtree import ppbtree

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
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

    def set_left(self, left_child):
        self.left = left_child
        if left_child:
            left_child.parent = self

    def set_right(self, right_child):
        self.right = right_child
        if right_child:
            right_child.parent = self

    def rotate_left(self):
        if self.right:
            old_child_left = self.right.left
            self.right.parent = self.parent
            self.right.set_left(self)
            self.set_right(old_child_left)

    def rotate_right(self):
        if self.left:
            old_child_right = self.left.right
            self.left.parent = self.parent
            self.left.set_right(self)
            self.set_left(old_child_right)

    def height(self, current_level=0):
        height_left = current_level
        height_right = current_level
        if self.left:
            height_left = self.left.height(current_level + 1)
        if self.right:
            height_right = self.right.height(current_level + 1)
        return max(height_left, height_right)

# for visual debugging purposes
EMPTY_NODE = BinaryTreeNode("x")

class BalancedBST:
    def __init__(self, root_val):
        self.root = BinaryTreeNode(root_val)

    # TODO implement this func
    def insert(self, value):
        self.root.insert(value)

    # TODO implement this func
    def remove(self, value):
        pass

    # Util debugging method to fix root
    def update_root(self):
        while (self.root.parent):
            self.root = self.root.parent

    def rotate_left(self):
        self.root.rotate_left()
        self.update_root()

    def rotate_right(self):
        self.root.rotate_right()
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
