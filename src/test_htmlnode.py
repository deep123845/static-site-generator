import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(None, None, None, {"href": "www.google.com"})
        props = ' href="www.google.com"'
        self.assertEqual(node.props_to_html(), props)
    def test_props2(self):
        node = HTMLNode(None, None, None, {"href": "www.google.com", "target": "_blank"})
        props = ' href="www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), props)
    def test_props3(self):
        node = HTMLNode(None, None, None, None)
        props = "" 
        self.assertEqual(node.props_to_html(), props)


if __name__ == "__main__":
    unittest.main()