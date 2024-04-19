import unittest
from penguin_with_gas_storage import dfs, checking_connection, reading_from_file, writing_to_the_file


class TestCheckingConnection(unittest.TestCase):
    def test_unreachable_storage(self):
        input_data = "input_unreachable.txt"
        cities, storage, pipelines = reading_from_file(input_data)
        unreachable = checking_connection(cities, storage, pipelines)
        output_data = "output_unreachable.txt"
        expected_output = read_output_data(output_data)
        self.assertEqual(unreachable, expected_output)

    def test_all_reachable(self):
        input_data = "input_all_reachable.txt"
        cities, storage, pipelines = reading_from_file(input_data)
        unreachable = checking_connection(cities, storage, pipelines)
        output_data = "output_all_reachable.txt"
        expected_output = read_output_data(output_data)
        self.assertEqual(unreachable, expected_output)

    def test_empty_input(self):
        input_data = "input_empty.txt"
        cities, storage, pipelines = reading_from_file(input_data)
        unreachable = checking_connection(cities, storage, pipelines)
        output_data = "output_empty.txt"
        expected_output = read_output_data(output_data)
        self.assertEqual(unreachable, expected_output)


def read_output_data(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [line.strip().split(", ") for line in lines]


if __name__ == "__main__":
    unittest.main()
