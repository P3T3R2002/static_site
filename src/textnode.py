class TextNode():
    def __init__(self, text="", text_type="", url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eg__(self, target):
        if (self.text == target.text and
            self.text_type == target.text_type and
            self.url == target.url)
            return True
        else: 
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def main():
    TextNode("This is a text node", "bold", https://www.boot.dev)
    