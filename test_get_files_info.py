import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):

    def test_current_directory(self):
        result = get_files_info("calculator", ".")
        print(f"\nResult for current directory: \n{result}")
        self.assertNotIn("Error:", result)

    def test_absolute_path_outside(self):
        result = get_files_info("calculator", "/bin")
        print(f"\nResult for '/bin' directory: \n{result}")
        self.assertIn("Error:", result)

    def test_child_directory(self):
        result = get_files_info("calculator", "pkg")
        print(f"\nResult for 'pkg' directory: \n{result}")
        self.assertNotIn("Error:", result)

    def test_parent_directory(self):
        result = get_files_info("calculator", "../")
        print(f"\nParent Directory: {result}")
        self.assertIn("Error:", result)

    def test_file_instead_of_directory(self):
        result = get_files_info("calculator", "main.py")
        print(f"\nResult for '../' directory: \n{result}")
        self.assertIn("Error:", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
