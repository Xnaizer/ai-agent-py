
import unittest
from functions.get_file_content import get_file_content


class TestGetFileContent(unittest.TestCase):

    def test_lorem_txt(self):
        result = get_file_content("calculator", "lorem.txt")
        print(f"\nlorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")

        self.assertIn("truncated", result)

    def test_main_py(self):
        result = get_file_content("calculator", "main.py")
        print(f"\nmain.py:\n{result}")

        self.assertIn("def main() -> None:", result)

    def test_calculator_py(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(f"\npkg/calculator.py:\n{result}")

        self.assertIn(
            "def _apply_operator(self, operators: list[str], values: list[float])",
            result
        )

    def test_absolute_path_outside(self):
        result = get_file_content("calculator", "/bin/cat")
        print(f"\n/bin/cat:\n{result}")

        self.assertIn("Error:", result)

    def test_nonexistent_file(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(f"\nNonexistent file:\n{result}")

        self.assertIn("pkg/does_not_exist.py", result)
        self.assertIn("Error:", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
