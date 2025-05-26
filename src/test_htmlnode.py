import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlnode = HTMLNode("p", "This is a paragraph", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })

        self.assertEqual(' href="https://www.google.com" target="_blank"', HTMLNode.props_to_html(htmlnode))

    def test_not_eq(self):
        htmlnode = HTMLNode("a", "This is a link", None, {
            "href": "https://www.facebook.com",
            "target": "_blank",
        })

        self.assertNotEqual(' href="https://www.google.com" target="_blank"', HTMLNode.props_to_html(htmlnode))

    def test_not_eq(self):
        htmlnode = HTMLNode("a", "This is a link", None, None)

        self.assertNotEqual(' href="https://www.google.com" target="_blank"', HTMLNode.props_to_html(htmlnode))

    def test_repr(self):
        htmlnode = HTMLNode("div", "I like Boot.dev", None, {"href": "boot.dev"})

        self.assertEqual(
            "HTMLNode(div, I like Boot.dev, children: None, {'href': 'boot.dev'})",
            htmlnode.__repr__()
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_a_more_props(self):
        node = LeafNode("a", "Click me!", {
            "href": "https://www.google.com",
            "class": "google",
            "target": "_blank"
        })
        expected_html = '<a href="https://www.google.com" class="google" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(), expected_html)

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

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

if __name__ == "__main__":
    unittest.main()