import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()