class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise  NotImplementedError("Not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        html = ""
        for prop in self.props:
            html = f'{html} {prop}="{self.props[prop]}"'
        return html
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        print("----", self.tag, self.value, self.props)
        if self.value == None:
            raise ValueError("no value")
        elif self.tag == None:
            return self.value
        else:
            prop = ""
            if self.props != None:
                prop = f"{self.props_to_html()}"
            return f'<{self.tag}{prop}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self, ):
        if self.children == None:
            raise ValueError("no children")
        elif self.tag == None:
            raise ValueError("no tag")
        else:
            childs = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children: 
                childs = f'{childs}\n{child.to_html()}'
            return f"{childs}\n</{self.tag}>"