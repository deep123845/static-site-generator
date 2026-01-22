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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.Plain,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.Plain),
                TextNode("image", TextType.Image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/Image.PNG)",
            TextType.Plain,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.Image, "https://www.example.COM/Image.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.Plain,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.Plain),
                TextNode("image", TextType.Image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.Plain),
                TextNode(
                    "second image", TextType.Image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.Plain,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Plain),
                TextNode("link", TextType.Link, "https://boot.dev"),
                TextNode(" and ", TextType.Plain),
                TextNode("another link", TextType.Link, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.Plain),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.Plain),
                TextNode("text", TextType.Bold),
                TextNode(" with an ", TextType.Plain),
                TextNode("italic", TextType.Italic),
                TextNode(" word and a ", TextType.Plain),
                TextNode("code block", TextType.Code),
                TextNode(" and an ", TextType.Plain),
                TextNode(
                    "obi wan image", TextType.Image, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.Plain),
                TextNode("link", TextType.Link, "https://boot.dev"),
            ],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()
