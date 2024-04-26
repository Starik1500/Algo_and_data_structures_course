import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from heap_based_priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_priority_queue(self):
        pq = PriorityQueue()
        pq.insert(5, 3)
        pq.insert(2, 1)
        pq.insert(3, 2)
        pq.insert(4, 5)
        pq.insert(5, 4)

        self.assertEqual(pq.inorder_traversal(), [(2, 1), (3, 2), (5, 3), (5, 4), (4, 5)])

        self.assertEqual(pq.peek(), 4)

        self.assertEqual(pq.pop(), 4)

        self.assertEqual(pq.inorder_traversal(), [(2, 1), (3, 2), (5, 3), (5, 4)])

if __name__ == "__main__":
    unittest.main()
