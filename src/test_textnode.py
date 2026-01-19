import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.Italic)
        node2 = TextNode("This is a different text node", TextType.Italic)
        self.assertNotEqual(node, node2)
    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.Link)
        node2 = TextNode("This is a text node", TextType.Link, "Test")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()