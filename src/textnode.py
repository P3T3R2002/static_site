from htmlnode import LeafNode

class TextNode():
    def __init__(self, text="", text_type="", url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(node1, node2):
        if (node1.text == node2.text and
            node1.text_type == node2.text_type and
            node1.url == node2.url):
            print("true")
            return True
        else: 
            print("false")
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
        match (self.text_type):
            case("text"):
                return LeafNode(None, self.text)
            case("bold"):
                return LeafNode("b", self.text)
            case("italic"):
                return LeafNode("i", self.text)
            case("code"):
                return LeafNode("code", self.text)
            case("link"):
                return LeafNode("a", self.text, {"href":self.url})
            case("image"):
                return LeafNode("img", "", {"scr":self.url, "alt":self.text})
            case _:
                raise Exception("Wrong type")
            

def main():
    TextNode("This is a text node", "bold", "https://www.boot.dev")
