import json
import unittest

from HomeExercise import verify_input


class TestVerifyInput(unittest.TestCase):
    def test_asterisk_count_zero(self):
        file_path = "test_data/test_policy_zero_asterisk.json"
        self.assertTrue(verify_input(file_path))

    def test_asterisk_count_one(self):
        file_path = "test_data/test_policy_one_asterisk.json"
        self.assertFalse(verify_input(file_path))

    def test_empty_file(self):
        file_path = "test_data/non_existent_file.json"
        with self.assertRaises(AssertionError):
            verify_input(file_path)

    def test_invalid_path_name(self):
        file_path = "test/data"
        with self.assertRaises(FileNotFoundError):
            verify_input(file_path)

    def test_empty_path_name(self):
        file_path = ""
        with self.assertRaises(ValueError):
            verify_input(file_path)

    def test_many_asterisks(self):
        file_path = "test_data/test_policy_many_sterisks.json"
        self.assertTrue(verify_input(file_path))

    def test_invalid_json(self):
        file_path = "test_data/invalid_json.txt"  # Provide a path to a file with invalid JSON syntax
        with self.assertRaises(ValueError):
            verify_input(file_path)

    def test_invalid_json_structure(self):
        file_path = "test_data/invalid_json_document_structure.json"  # Provide a path to a file with invalid JSON syntax
        with self.assertRaises(KeyError):
            verify_input(file_path)

if __name__ == '__main__':
    unittest.main()
