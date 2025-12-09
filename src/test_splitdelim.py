import unittest
from textnode import TextNode, TextType
from main import split_nodes_delimiter


class TestSplitDelimiter(unittest.TestCase):
    def test_code_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(new_nodes, expected_nodes)

    def test_bold_node(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(new_nodes, expected_nodes)

    def test_multiple_delimiters(self):
        node = TextNode("This is **bold** and this is **also bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("also bold", TextType.BOLD),
        ]

        self.assertListEqual(new_nodes, expected_nodes)

    def test_mixed_nodes_input(self):
        nodes = [
            TextNode("This is text", TextType.TEXT),
            TextNode("This is already bold", TextType.BOLD),
            TextNode("and this is `code`", TextType.TEXT),
        ]

        new_nodes = split_nodes_delimiter([nodes], "`", TextType.CODE)

        expected_nodes = [
            TextNode("This is text", TextType.TEXT),
            TextNode("This is already bold", TextType.BOLD),
            TextNode("and this is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]

        self.assertListEqual(new_nodes, expected_nodes)

    def test_raises_exception_for_unclosed_tag(self):
        node = TextNode("This has an unclosed `code block", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()
