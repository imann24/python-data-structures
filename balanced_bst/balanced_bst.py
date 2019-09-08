from lib.pptree import pptree

class BinaryTreeNode:
    def __init__(self, value, flag=None):
        self.value = value
        self.left = None
        self.right = None
        self.flag = flag
        self.children = []

    def __str__(self):
        """
        TODO: revise pptree module to always print children[0] on left
              this will make the flag property unecessary for debugging
        """
        if self.flag:
            return "{} ({})".format(self.value, self.flag)
        return str(self.value)

    def __insert_left(self, value):
        if self.left:
            self.left.insert(value)
        else:
            self.left = BinaryTreeNode(value, "L")

    def __insert_right(self, value):
        if self.right:
            self.right.insert(value)
        else:
            self.right = BinaryTreeNode(value, "R")

    # TODO: handle self-balancing in this function
    def insert(self, value):
        if value <= self.value:
            self.__insert_left(value)
        else:
            self.__insert_right(value)
        self.__update_children()

    # Helper function to maintain compatibility with 'pptree' debugging
    def __update_children(self):
        self.children = [EMPTY_NODE if (self.left == None) else self.left,
                         EMPTY_NODE if (self.right == None) else self.right]

# for visual debugging purposes
EMPTY_NODE = BinaryTreeNode("|")

class BalancedBST:
    def __init__(self, root_val):
        self.root = BinaryTreeNode(root_val)

    # TODO implement this func
    def insert(self, value):
        self.root.insert(value)

    # Return True or False for if tree contains
    # TODO
    def search(self, value):
        pass

    # Returns number (heigh of tree)
    # TODO
    def height(self):
        pass

    # Prints a visual representation of tree
    def pretty_print(self):
        pptree.print_tree(self.root)
