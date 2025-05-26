import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("Testing equal nodes with optional link parameter", TextType.IMAGE, "link.com")
        node2 = TextNode("Testing equal nodes with optional link parameter", TextType.IMAGE, "link.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Testing not equal nodes", TextType.CODE, "www.wtf.com")
        node2 = TextNode("Testing not equal nodes", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.CODE, "link.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "link.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()