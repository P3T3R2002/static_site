import unittest

from textnode import *
from split_node import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        nodes = ([  TextNode("This is a test **bold**", "bold"),
                    TextNode("This is a test *italic*", "italic"),
                    TextNode("This is a test`code`", "code"),
                    TextNode("This is a test link", "link", "https://www.boot.dev"),
                    TextNode("This is a test image", "image", "https://www.boot.dev"),
        ])

        node_code = [
                        TextNode("This is text with a `code block` word", "text"),
                        TextNode("This is a `testcode`", "text")
                    ]
        code_nodes = split_nodes_delimiter(node_code, "`", "code")
        for i in range(0, len(code_nodes)):
            print("----", code_nodes[i].text_node_to_html_node().to_html())

        node_bold = [
                        TextNode("This is text with a **bold block** word", "text"),
                        TextNode("This is a **testcode**", "text")
                    ]
        bold_nodes = split_nodes_delimiter(node_bold, "**", "bold")
        for i in range(0, len(bold_nodes)):
            print("----", bold_nodes[i].text_node_to_html_node().to_html())

        node_italic = [
                        TextNode("This is text with a *italic block* word", "text"),
                        TextNode("This is a *testcode*", "text")
                    ]
        italic_nodes = split_nodes_delimiter(node_italic, "*", "italic")
        for i in range(0, len(italic_nodes)):
            print("----", italic_nodes[i].text_node_to_html_node().to_html())

   

if __name__ == "__main__":
    unittest.main()
