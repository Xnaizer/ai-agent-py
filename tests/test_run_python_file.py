import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def test_run_code_main_without_argument(self):
        result = run_python_file("calculator", "main.py")
        print(f"\nmain.py:\n{result}")
        self.assertIn("<expression>", result)
    
    def test_run_code_main(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(f"\nmain.py:\n{result}")
        self.assertIn("8", result)

    def test_run_code_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(f"\ntests.py:\n{result}")
        self.assertIn("....", result)

    def test_run_code_outside_parent(self):
            result = run_python_file("calculator", "../main.py")
            print(f"\n../main.py:\n{result}")
            self.assertIn("it is outside the permitted working directory", result)

    def test_run_code_non_exist(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(f"\nnonexistent.py:\n{result}")
        self.assertIn("does not exist or is not a regular file", result)

    def test_run_code_non_python(self):
        result = run_python_file("calculator", "lorem.txt")
        print(f"\nnonexistent.py:\n{result}")
        self.assertIn("is not a Python file", result)


        

if __name__ == "__main__":
    unittest.main(verbosity=2)