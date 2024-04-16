import unittest
from matrix_bfs import bfs, main, is_valid, create_coordinate, create_queue_node


class TestShortestPath(unittest.TestCase):
    def test_write_output_file(self):
        input_file = "input_with_path.txt"
        output_file = "test_output_with_path.txt"
        start_point, end_point, mat = main(input_file)
        shortest_distance = bfs(mat, start_point, end_point)
        main(output_file, shortest_distance)
        with open(output_file, "r") as file:
            output_data = int(file.read().strip())
        self.assertEqual(output_data, 12)

    def test_no_path(self):
        input_file = "input_no_path.txt"
        output_file = "test_output_no_path.txt"
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
