import unittest
from inverting_binary_tree import BinaryTree, invert_binary_tree


class TestBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = BinaryTree(9)
        root.left = BinaryTree(6)
        root.right = BinaryTree(3)
        self.assertEqual(root.value, 9)
        self.assertEqual(root.left.value, 6)
        self.assertEqual(root.right.value, 3)
        inverted_root = invert_binary_tree(root)


if __name__ == "__main__":
    unittest.main()
