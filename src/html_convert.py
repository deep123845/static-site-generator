from block import *
from text import *
from htmlnode import *
from textnode import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    inner_html = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.NORMAL:
                inner_html.append(normal_to_html_node(block))
            case BlockType.HEADING:
                inner_html.append(heading_to_html_node(block))
            case BlockType.CODE:
                inner_html.append(code_to_html_node(block))
            case BlockType.QUOTE:
                inner_html.append(quote_to_html_node(block))
            case BlockType.UNORDERED:
                inner_html.append(ul_to_html_node(block))
            case BlockType.ORDERED:
                inner_html.append(ol_to_html_node(block))

    parent = ParentNode("div", inner_html)

    return parent


def normal_to_html_node(block):
    inner_html = text_to_children(block)
    parent = ParentNode("p", inner_html)
    return parent


def heading_to_html_node(block):
    num_heading = 0
    for i in range(6):
        if block[i] == "#":
            num_heading += 1

    inner_html = text_to_children(block[num_heading + 1 :])
    parent = ParentNode(f"h{num_heading}", inner_html)
    return parent


def code_to_html_node(block):
    block = "\n".join(block.split("\n")[1:-1]) + "\n"
    inner_text = TextNode(block, TextType.Code)
    inner_html = [text_node_to_html_node(inner_text)]
    parent = ParentNode("pre", inner_html)
    return parent


def quote_to_html_node(block):
    block = block.replace("> ", "")
    inner_html = text_to_children(block)
    parent = ParentNode("blockquote", inner_html)
    return parent


def ul_to_html_node(block):
    lines = block.split("\n")
    inner_html = []
    for line in lines:
        line = line[2:]
        list_html = text_to_children(line)
        inner_html.append(ParentNode("li", list_html))
    return ParentNode("ul", inner_html)


def ol_to_html_node(block):
    lines = block.split("\n")
    inner_html = []
    for line in lines:
        line = line[line.find(" ") + 1 :]
        list_html = text_to_children(line)
        inner_html.append(ParentNode("li", list_html))
    return ParentNode("ol", inner_html)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))

    return html_nodes
