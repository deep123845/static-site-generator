from textnode import *
from htmlnode import *
from text import *


def main():
    node = TextNode("text is **bold** **text**", TextType.Plain)
    new_nodes = split_nodes_delimiter([node], "**", TextType.Bold)
    print(new_nodes)


main()
