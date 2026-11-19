import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):

    def test_write_lorem(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(f"\nlorem.txt:\n{result}")
        self.assertIn("Successfully wrote to", result)

    def test_write_morelorem(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(f"\npkg/morelorem.txt:\n{result}")
        self.assertIn("Successfully wrote to", result)

    def test_write_temp(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(f"\n/tmp/temp.txt:\n{result}")
        self.assertIn("outside the permitted working directory", result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
      