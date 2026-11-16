
import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):

    def test_current_directory(self):
        result = get_files_info("calculator", ".")
        print(f"\nCurrent Directory: {result}")
        self.assertIn("Success:", result)

    def test_absolute_path_outside(self):
        result = get_files_info("calculator", "/bin")
        print(f"\nAbsolute Path: {result}")
        self.assertIn("Error:", result)

    def test_parent_directory(self):
        result = get_files_info("calculator", "../")
        print(f"\nParent Directory: {result}")
        self.assertIn("Error:", result)

    def test_file_instead_of_directory(self):
        result = get_files_info("calculator", "main.py")
        print(f"\nFile Instead of Directory: {result}")
        self.assertIn("Error:", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
