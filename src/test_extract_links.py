import unittest

from inline_markdown import (
    extract_markdown_images, 
    extract_markdown_links,
)

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images_basic(self):
        text = "![alt text](https://example.com/image.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [('alt text', 'https://example.com/image.jpg')])

    def test_extract_markdown_images_multiple(self):
        text = "![first](https://example.com/first.jpg) and ![second](https://example.com/second.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [
            ('first', 'https://example.com/first.jpg'),
            ('second', 'https://example.com/second.jpg')
        ])

    def test_extract_markdown_images_none(self):
        text = "No images here."
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_extract_markdown_images_malformed(self):
        text = "![alt text missing closing parenthesis"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_extract_markdown_links_basic(self):
        text = "[link text](https://example.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [('link text', 'https://example.com')])

    def test_extract_markdown_links_multiple(self):
        text = "[first link](https://example.com/1) and [second link](https://example.com/2)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [
            ('first link', 'https://example.com/1'),
            ('second link', 'https://example.com/2')
        ])

    def test_extract_markdown_links_none(self):
        text = "No links here."
        result = extract_markdown_links(text)
        self.assertEqual(result, [])