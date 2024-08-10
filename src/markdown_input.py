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


def markdown_to_html(markdown):
    block_and_type = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_and_type.append((block, block_type))
    block_to_html(block_and_type)

def block_to_html(blocks):
    list_of_textnodes = []
    list_of_nodes = []
    for block in blocks:
        list_of_textnodes.append(text_to_textnodes(block[0]))
        print(list_of_textnodes[-1:])
    
    for textnodes in list_of_textnodes:
        if len(textnodes) == 1:
            pass





 