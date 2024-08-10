import unittest
from markdown_input import *

class TestInput(unittest.TestCase):
    def test_eq(self):
        if True:
            with open("./src/markdown_input.md") as f:
                file_contents = f.read()
            markdown_to_html(file_contents)


if __name__ == "__main__":
    unittest.main()