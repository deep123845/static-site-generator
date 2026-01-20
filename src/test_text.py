import unittest
from text import *
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.Plain)
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Plain),
                TextNode("bolded", TextType.Bold),
                TextNode(" word", TextType.Plain),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.Plain
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Plain),
                TextNode("bolded", TextType.Bold),
                TextNode(" word and ", TextType.Plain),
                TextNode("another", TextType.Bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.Plain
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Plain),
                TextNode("bolded word", TextType.Bold),
                TextNode(" and ", TextType.Plain),
                TextNode("another", TextType.Bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.Plain)
        new_nodes = split_nodes_delimiter([node], "_", TextType.Italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.Plain),
                TextNode("italic", TextType.Italic),
                TextNode(" word", TextType.Plain),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.Plain)
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.Italic)
        self.assertListEqual(
            [
                TextNode("bold", TextType.Bold),
                TextNode(" and ", TextType.Plain),
                TextNode("italic", TextType.Italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.Plain)
        new_nodes = split_nodes_delimiter([node], "`", TextType.Code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Plain),
                TextNode("code block", TextType.Code),
                TextNode(" word", TextType.Plain),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
