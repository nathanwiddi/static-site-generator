import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        node = HTMLNode('a', 'html tag here', None, props=props)
        expected_repr = "HTMLNode(a, html tag here, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), expected_repr)  # Test __repr__

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode('a', 'html tag here', None, props=props)
        expected_props_html = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props_html)  # Test props_to_html

    def test_props_to_html_single_prop(self):
        props = {
        "class": "btn"
        }
        node = HTMLNode(props=props)
        expected_props_html = ' class="btn"'
        self.assertEqual(node.props_to_html(), expected_props_html)  # Test props_to_html

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        expected_props_html = ""
        self.assertEqual(node.props_to_html(), expected_props_html)  # Test props_to_html


    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_leaf_noprops(self):
        leafnode = LeafNode("p", "This is a paragraph of text.")
        expected_props_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(leafnode.to_html(), expected_props_html)  # Test props_to_html
    
    def test_leaf_props(self):
        leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_props_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(leafnode.to_html(), expected_props_html)  # Test props_to_html
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    
    def test_parentnode_tohtml(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

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

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":

    unittest.main()