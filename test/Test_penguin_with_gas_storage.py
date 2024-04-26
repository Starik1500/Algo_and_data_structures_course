import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from penguin_with_gas_storage import dfs, checking_connection

class TestCheckingConnection(unittest.TestCase):
    def test_unreachable_storage(self):
        cities = ['A', 'B', 'C', 'D', 'E']
        storage = ['A', 'B']
        pipelines = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')]
        unreachable = checking_connection(cities, storage, pipelines)
        expected_output = []
        self.assertEqual(unreachable, expected_output)

    def test_all_reachable(self):
        cities = ['A', 'B', 'C', 'D']
        storage = ['A', 'B']
        pipelines = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        unreachable = checking_connection(cities, storage, pipelines)
        expected_output = []
        self.assertEqual(unreachable, expected_output)

    def test_empty_input(self):
        cities = []
        storage = []
        pipelines = []
        unreachable = checking_connection(cities, storage, pipelines)
        expected_output = []
        self.assertEqual(unreachable, expected_output)

if __name__ == "__main__":
    unittest.main()