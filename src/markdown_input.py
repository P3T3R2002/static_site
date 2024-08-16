from htmlnode import *
from split_node import *

def markdown_to_blocks(markdown):
    removed = 0
    split = markdown.split("\n\n")
    for i in range(0, len(split)):
        j = i-removed
        if split[j] == "":
            trash = split.pop(j)
            removed += 1
        else:
            split[j] = split[j].strip("\n")
            split[j] = split[j].strip()

    return split

def block_to_block_type(md_block):
    match (md_block[0]):
        case("#"):
            for i in range(1, 7):
                if md_block[i] == " ":
                    return f"heading {i}"
                elif md_block[i] != "#":
                    return "paragraph"
            return "paragraph"

        case("`"):
            if (md_block[1] == "`" and 
                md_block[2] == "`" and 
                md_block[-1] == "`" and 
                md_block[-2] == "`" and 
                md_block[-3] == "`"):
                return "code"
            else:
                return "paragraph"

        case(">"):
            return "quote"

        case("-"):
            return unordered(md_block, "-")
        case("*"):
            return unordered(md_block, "*")

        case("1"):
            ord_list = md_block.split("\n")
            for i in range(0, len(ord_list)):
                if ord_list[i][0:3] != f"{i+1}. ":
                    if len(ord_list) == 1:
                        return "paragraph"
                    raise Exception("The ordered list is wrong")
            return "ordered_list"

        case _:
            return "paragraph"

def unordered(block, pre):
    unord_list = block.split("\n")
    if unord_list[0][0:2] != f"{pre} ":
        return "paragraph"
    for i in range(0, len(unord_list)):
        if unord_list[i][0:2] == "* " or unord_list[i][0:2] == "- ":
            return "unordered_list"
        else:
            raise Exception("The unordered list is wrong")

def block_to_html(blocks):
    list_of_htmlnode = []
    list_of_textnodes = []
    for block in blocks:
        split = text_to_textnodes(block[0], block[1])
        new_split = []
        
        for node in split:
            textnodes = text_to_textnodes(node.text)
            
            if len(textnodes) != 1:
                new_split.append(textnodes)
            else: new_split.append(node)
        list_of_textnodes.append((new_split, block[1]))
    
    for textnodes in list_of_textnodes:
        match(textnodes[1].split(" ")[0]):
            case("heading"):
                for textnode in textnodes[0]:
                    textnode.text = textnode.text.lstrip("#").strip()
                if len(textnodes[0]) == 1:
                    list_of_htmlnode.append(textnodes[0][0].text_node_to_html_node(f"h{textnodes[1].split(' ')[1]}"))
                else:
                   list_of_htmlnode.append(ParentNode(f"h{textnodes[1].split(' ')[1]}", get_list_of_children(textnodes[0]))) 

            case("paragraph"):
                list_of_htmlnode.append(ParentNode("p", get_list_of_children(textnodes[0])))
            
            case("code"):
                list_of_htmlnode.append(ParentNode("pre", [LeafNode("code", textnodes[0][0].text)]))
            
            case("quote"):
                textnodes[0][0].text = textnodes[0][0].text.lstrip(">").strip()
                list_of_htmlnode.append(LeafNode("blockquote", textnodes[0][0].text.replace(">", "")))
            
            case("unordered_list"):
                list_of_htmlnode.append(ParentNode("ul", get_list_of_children(textnodes[0], "li")))
            
            case("ordered_list"):
                list_of_htmlnode.append(ParentNode("ol", get_list_of_children(textnodes[0], "li")))
            
            case _:
                raise Exception("wrong text type in block to html")      
    return list_of_htmlnode

def get_list_of_children(lst, unique = None):
    children = []
    for item in lst:
        if isinstance(item, list):
            ch = get_list_of_children(item)
            children.append(ParentNode(unique, ch))
        else:
            children.append(item.text_node_to_html_node(unique))
    return children

def markdown_to_html(markdown):
    block_and_type = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_and_type.append((block, block_type))
    return block_to_html(block_and_type)



 