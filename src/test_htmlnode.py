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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_many_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("a", "Google", {"href": "https://www.google.com"})
        grandchild_node3 = LeafNode("p", "paragraph paragraph")
        child_node = ParentNode("span", [grandchild_node])
        child_node2 = ParentNode("div", [grandchild_node2, grandchild_node3])
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b>grandchild</b></span><div><a href="https://www.google.com">Google</a><p>paragraph paragraph</p></div></div>',
        )


if __name__ == "__main__":
    unittest.main()
