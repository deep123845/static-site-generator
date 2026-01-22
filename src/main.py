from textnode import *
from htmlnode import *
from text import *


def main():
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.Plain,
    )
    nodes = split_nodes_image([node])
    print(nodes)


main()
