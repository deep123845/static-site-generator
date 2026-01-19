import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(None, None, None, {"href": "www.google.com"})
        props = ' href="www.google.com"'
        self.assertEqual(node.props_to_html(), props)

    def test_props2(self):
        node = HTMLNode(
            None, None, None, {"href": "www.google.com", "target": "_blank"}
        )
        props = ' href="www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), props)

    def test_props3(self):
        node = HTMLNode(None, None, None, None)
        props = ""
        self.assertEqual(node.props_to_html(), props)

    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Google", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Google</a>')


if __name__ == "__main__":
    unittest.main()
