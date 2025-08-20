from textnode import TextNode, TextType
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode("", {text_node.text})
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", {text_node.text})
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", {text_node.text})
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", {text_node.text})
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", {text_node.text}, "href")
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            "img",
            "",
            "src",
            "alt",
        )

    else:
        raise Exception("TextNode has none of the required types")
