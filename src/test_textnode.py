import unittest

from textnode import *
from split_node import *
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        
        text_node1 = text_to_textnodes("This is **bold** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        for node1 in text_node1:
            print(node1)
        print("\n")
        text_node1 = text_to_textnodes("This is *italic* with an **bold** word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        for node1 in text_node1:
            print(node1)
        print("\n")
        text_node1 = text_to_textnodes("This is `code block` with an *italic* word and a **bold** and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        for node1 in text_node1:
            print(node1)
        print("\n")
        text_node1 = text_to_textnodes("This is ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) with an *italic* word and a `code block` and an **bold** and a [link](https://boot.dev)")
        for node1 in text_node1:
            print(node1)
        print("\n")
        text_node1 = text_to_textnodes("This is *italic* with an [link](https://boot.dev) word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a **bold**")
        for node1 in text_node1:
            print(node1)
        print("\n")

        text_node1 = text_to_textnodes("This is **bold** with an **italic** word and a **code block** and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        for node1 in text_node1:
            print(node1)
        print("\n")
        text_node1 = text_to_textnodes("This is *bold* with an *italic* word and a *code block* and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        for node1 in text_node1:
            print(node1)
        print("\n")
        text_node1 = text_to_textnodes("This is `bold` with an `italic` word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        for node1 in text_node1:
            print(node1)
        print("\n")
        text_node1 = text_to_textnodes("This is ![ob wan image](https://i.imgur.com/fJRm4Vk.jpeg) with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        for node1 in text_node1:
            print(node1)
        print("\n")
        text_node1 = text_to_textnodes("This is **bold** with an [link](https://boot.dev) word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        for node1 in text_node1:
            print(node1)
        print("\n")



if __name__ == "__main__":
    unittest.main()
