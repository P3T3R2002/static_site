from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []
    for old_node in old_nodes:
        current_type = old_node.text_type
        split = old_node.text.split(delimiter)
        for text in split:
            if text != "":
                new_node.append(TextNode(text, current_type))
                if current_type == text_type:
                    current_type = old_node.text_type
                else:current_type = text_type

            
    return new_node