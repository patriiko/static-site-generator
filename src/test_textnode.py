import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "www.boot.dev"})

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
            "src": "www.boot.dev",
            "alt": "This is an image"
        })

        
if __name__ == "__main__":
    unittest.main()