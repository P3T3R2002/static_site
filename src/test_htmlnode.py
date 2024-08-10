import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        if False:
            node = ParentNode(
                "p1",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    ParentNode(
                        "p2",
                        [
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text")
                        ]
                    ), 
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ]
            ) 
            print(node.to_html())
            
        

if __name__ == "__main__":
    unittest.main()
