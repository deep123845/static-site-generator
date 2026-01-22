from textnode import *
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.Plain:
            new_nodes.append(old_node)
            continue
        text_segments = old_node.text.split(delimiter)
        if len(text_segments) % 2 == 0:
            raise Exception("Invalid makdown syntax")
        for i in range(len(text_segments)):
            if text_segments[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text_segments[i], TextType.Plain))
            else:
                new_nodes.append(TextNode(text_segments[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
