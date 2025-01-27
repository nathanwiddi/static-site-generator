import unittest
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link, 
    text_to_textnodes
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_delimiter(self):
        # Test delimiter-based splitting
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_image(self):
        # Test image parsing
        node = TextNode(
            "Text with an image ![example](https://example.com/image.png)", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text with an image ", TextType.TEXT),
                TextNode("example", TextType.IMAGE, "https://example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_nodes_link(self):
        # Test link parsing
        node = TextNode(
            "Check [this site](https://example.com) for more info.", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Check ", TextType.TEXT),
                TextNode("this site", TextType.LINK, "https://example.com"),
                TextNode(" for more info.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )


    def test_basic_markdown_parsing(self):
        """
        Test parsing of bold, italic, code, image, and link formatting in a markdown-like text.
        """
        test_text = (
            "This is **bold text** with an *italic* word, a `code block`, "
            "an ![image](https://example.com/image.png), "
            "and a [link](https://example.com)."
        )
        result = text_to_textnodes(test_text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word, a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(", an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(", and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_unmatched_delimiter_raises_error(self):
        """
        Test that unmatched delimiters (e.g., a single `*` or `**`) raise a ValueError.
        """
        test_text = "This is **bold text* with an unmatched delimiter."
        with self.assertRaises(ValueError) as context:
            text_to_textnodes(test_text)

        self.assertIn("Invalid markdown", str(context.exception))

    def test_text_with_no_markdown(self):
        """
        Test that text with no markdown formatting is returned as a single TEXT node.
        """
        test_text = "This is plain text with no markdown."
        result = text_to_textnodes(test_text)

        expected = [
            TextNode("This is plain text with no markdown.", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
