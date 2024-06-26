import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from last_index import pattern_search

class TestPatternSearch(unittest.TestCase):
    def test_pattern_search(self):
        first_haystack = "AABAACAADAABAABA"
        first_needle = "AABA"
        first_last_index, first_comparisons = pattern_search(first_haystack, first_needle)
        self.assertEqual(first_last_index, 12)
        self.assertEqual(first_comparisons, 30)

        second_haystack = "ABCDEF"
        second_needle = "XYZ"
        second_last_index, second_comparisons = pattern_search(second_haystack, second_needle)
        self.assertEqual(second_last_index, -1)
        self.assertEqual(second_comparisons, 4)

if __name__ == "__main__":
    unittest.main()
