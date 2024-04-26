import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
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
        root = BinaryTree(9)
        root.left = BinaryTree(6)
        root.right = BinaryTree(3)
        self.assertEqual(inverted_root.value, 9)
        self.assertEqual(inverted_root.left.value, 3)
        self.assertEqual(inverted_root.right.value, 6)

if __name__ == "__main__":
    unittest.main()
