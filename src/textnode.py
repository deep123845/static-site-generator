from enum import Enum
from htmlnode import *


class TextType(Enum):
    Plain = "plain"
    Bold = "bold"
    Italic = "italic"
    Code = "code"
    Link = "link"
    Image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            (self.text == other.text)
            and (self.text_type == other.text_type)
            and (self.url == other.url)
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.Plain:
            return LeafNode(None, text_node.text)
        case TextType.Bold:
            return LeafNode("b", text_node.text)
        case TextType.Italic:
            return LeafNode("i", text_node.text)
        case TextType.Code:
            return LeafNode("code", text_node.text)
        case TextType.Link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.Image:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Error, Invalid Text Type")
