import unittest
from markdown_input import *

class TestInput(unittest.TestCase):
    def test_eq(self):
        if True:
            with open("./src/markdown_input.md") as f:
                file_contents = f.read()
            htmlnodes = markdown_to_html(file_contents)
            for htmlnode in htmlnodes:
                print("////\n", htmlnode.to_html())

if __name__ == "__main__":
    unittest.main()