import re
from textnode import *


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []
    for old_node in old_nodes:
        current_type = old_node.text_type
        split = old_node.text.split(delimiter)
        if len(split) != 1:
            for text in split:
                new_node.append(TextNode(text, current_type)) 
                if current_type == text_type:
                    current_type = old_node.text_type
                else:current_type = text_type  
                if new_node[-1].text == "":
                    trash = new_node.pop() 
        else: new_node.append(old_node)   
    return new_node

def split_nodes_links(old_nodes):
    split = []
    for old_node in old_nodes:
        links = []
        links.append(extract_markdown_links(old_node.text))
        if links == [[]]:
            split.append(old_node)
        for link in links:   
            for lnk in link:
                split.append(TextNode(old_node.text.split(f"[{lnk[0]}]({lnk[1]})")[0], old_node.text_type))
                left_over = TextNode(old_node.text.split(f"[{lnk[0]}]({lnk[1]})")[1], old_node.text_type)
                old_node.text = old_node.text.replace(split[-1].text, "")
                split.append(TextNode(lnk[0], "link", lnk[1]))
                old_node.text = old_node.text.replace(f"[{lnk[0]}]({lnk[1]})", "")
                if left_over.text != "":
                    split.append(left_over)
    return split

# images/links = list of lists of the extracted images/links
# split = list of the splitted old_nodes
# old_nodes = list of TextNodes

def split_nodes_images(old_nodes):
    split = []
    for old_node in old_nodes:
        images = []
        images.append(extract_markdown_images(old_node.text))
        if images == [[]]:
            split.append(old_node)
        else:
            for image in images:   
                for img in image:
                    split.append(TextNode(old_node.text.split(f"![{img[0]}]({img[1]})")[0], old_node.text_type))
                    left_over = TextNode(old_node.text.split(f"[{img[0]}]({img[1]})")[1], old_node.text_type)
                    old_node.text = old_node.text.replace(split[-1].text, "")
                    split.append(TextNode(img[0], "image", img[1]))
                    old_node.text = old_node.text.replace(f"![{img[0]}]({img[1]})", "")
                    if left_over.text != "":
                        split.append(left_over)
    return split

def text_to_textnodes(text, list_type = None):
    split = [TextNode(text, "text")]
    if list_type == "ordered_list":
        split = split_ordered(split)
    elif list_type == "unordered_list":
            split = split_unordered(split)     
    else:
        split = split_nodes_delimiter(split, "**", "bold")
        split = split_nodes_delimiter(split, "*", "italic")
        split = split_nodes_delimiter(split, "`", "code")
        split = split_nodes_images(split)
        split = split_nodes_links(split)
    
    return split

def split_unordered(old_node):
    new_node = []
    split = old_node[0].text.split("\n")
    for text in split:
        if text != "":
            new_node.append(TextNode(text.lstrip("*").lstrip("-").strip(), old_node[0].text_type))
    return new_node

def split_ordered(old_node):
    i = 1
    new_node = []
    split = old_node[0].text.split("\n")
    for text in split:
        if text != "":
            new_node.append(TextNode(text.lstrip(f"{i}.").strip(), old_node[0].text_type))
            i += 1
    return new_node
