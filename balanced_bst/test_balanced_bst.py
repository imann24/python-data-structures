from balanced_bst import BalancedBST, BinaryTreeNode

MARKER = "======================="

def test_can_init():
    root_val = 5
    search_tree = BalancedBST(root_val)

    assert search_tree
    assert search_tree.root
    assert search_tree.root.value == root_val
    assert search_tree.height() == 1
    assert search_tree.root.height() == 0

    search_tree.pretty_print()

def test_insert_less():
    root_val = 5
    less_val = 2
    search_tree = BalancedBST(root_val)

    search_tree.insert(less_val)

    assert search_tree
    assert search_tree.root
    assert search_tree.root.value == root_val
    assert search_tree.root.left
    assert search_tree.root.left.value == less_val
    assert search_tree.height() == 2

    search_tree.pretty_print()

def test_insert_more():
    root_val = 5
    more_val = 10
    search_tree = BalancedBST(root_val)

    search_tree.insert(more_val)

    assert search_tree
    assert search_tree.root
    assert search_tree.root.value == root_val
    assert search_tree.root.right
    assert search_tree.root.right.value == more_val
    assert search_tree.height() == 2

    search_tree.pretty_print()

def test_insert_both():
    root_val = 5
    less_val = 2
    more_val = 10
    search_tree = BalancedBST(root_val)

    search_tree.insert(less_val)
    search_tree.insert(more_val)

    assert search_tree
    assert search_tree.root
    assert search_tree.root.value == root_val
    assert search_tree.root.left
    assert search_tree.root.left.value == less_val
    assert search_tree.root.right
    assert search_tree.root.right.value == more_val
    assert search_tree.height() == 2

    search_tree.pretty_print()

def test_many_insertions():
    search_tree = BalancedBST(5)
    values_to_insert = [1, 2, 3, 50, 200, 20, 1, 3, 4, 4, 10, 1, 40, 21, 15, 5]
    # TODO: add asserts here
    for val in values_to_insert:
        search_tree.insert(val)
    search_tree.pretty_print()

def test_manual_left_rotation():
    search_tree = BalancedBST(1)

    search_tree.insert(2)
    search_tree.insert(3)

    print()
    print("Before Rotation:")
    search_tree.pretty_print()
    print()

    search_tree.rotate_left()
    search_tree.update_root()
    print("After Rotation:")
    search_tree.pretty_print()

    assert search_tree.root.value == 2
    assert search_tree.root.left.value == 1
    assert search_tree.root.right.value == 3
    assert search_tree.height() == 2

def test_manual_right_rotation():
    search_tree = BalancedBST(3)
    search_tree.insert(2)
    search_tree.insert(1)

    print()
    print("Before Rotation:")
    search_tree.pretty_print()
    print()

    search_tree.rotate_right()
    print("After Rotation:")
    search_tree.pretty_print()

    assert search_tree.root.value == 2
    assert search_tree.root.left.value == 1
    assert search_tree.root.right.value == 3
    assert search_tree.height() == 2

if __name__ == "__main__":
    tests_to_run = [test_can_init,
                    test_insert_less,
                    test_insert_more,
                    test_insert_both,
                    test_many_insertions,
                    test_manual_left_rotation,
                    test_manual_right_rotation]

    for run_test in tests_to_run:
        print(MARKER)
        print("{}:".format(run_test.__name__))
        run_test()
        print(MARKER)
        print()
