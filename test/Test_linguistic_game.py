import unittest
import os
import sys

test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(
    os.path.join(os.path.dirname(test_file_path), os.pardir)
)
src_path = os.path.join(common_parent_path, "src")
sys.path.append(src_path)
from linguistic_game import (
    longest_word_chain,
    comparing,
    read_input_data,
    write_output_data,
)


class TestLongestWordChain(unittest.TestCase):
    def test_comparing(self):
        self.assertEqual(comparing("abc", "bcd"), 2)
        self.assertEqual(comparing("cat", "dog"), 0)
        self.assertEqual(comparing("abcdef", "abdef"), 5)

    def test_longest_word_chain(self):
        self.assertEqual(longest_word_chain(["cat", "cats", "cast", "at", "sat"]), 4)
        self.assertEqual(longest_word_chain(["cat", "dog", "bat", "sat"]), 1)
        self.assertEqual(longest_word_chain(["a", "aa", "aaa", "aaaa"]), 4)

    def test_read_input_data(self):
        current_dir = os.path.dirname(__file__)
        input_filename = os.path.join(current_dir, "test_wchain_input.in")
        words = read_input_data(input_filename)
        self.assertEqual(words, ["cat", "cats", "cast", "at", "sat"])

if __name__ == "__main__":
    unittest.main()
