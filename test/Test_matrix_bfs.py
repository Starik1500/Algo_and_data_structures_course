import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from matrix_bfs import bfs, main, is_valid

class TestShortestPath(unittest.TestCase):
    def test_write_output_file(self):
        input_file = os.path.join(os.path.dirname(__file__), "input_with_path.txt")
        output_file = os.path.join(os.path.dirname(__file__), "test_output_with_path.txt")
        start_point, end_point, mat = main(input_file)
        shortest_distance = bfs(mat, start_point, end_point)
        main(output_file, shortest_distance)
        with open(output_file, "r") as file:
            output_data = int(file.read().strip())
        self.assertEqual(output_data, 12)

    def test_no_path(self):
        input_file = os.path.join(os.path.dirname(__file__), "input_no_path.txt")
        output_file = os.path.join(os.path.dirname(__file__), "test_output_no_path.txt")
        start_point, end_point, mat = main(input_file)
        shortest_distance = bfs(mat, start_point, end_point)
        main(output_file, shortest_distance)
        with open(output_file, "r") as file:
            output_data = int(file.read().strip())
        self.assertEqual(output_data, -1)

    def test_valid(self):
        ROW = 11
        COL = 10
        self.assertTrue(is_valid(0, 0))
        self.assertTrue(is_valid(5, 5))
        self.assertTrue(is_valid(ROW - 1, COL - 1))

    def test_invalid(self):
        ROW = 11
        COL = 10
        self.assertFalse(is_valid(-1, 0))
        self.assertFalse(is_valid(0, -1))
        self.assertFalse(is_valid(ROW, COL))

if __name__ == "__main__":
    unittest.main()