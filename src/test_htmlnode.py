import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(
            "<p>",
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        print(node1.props_to_html())

    # def second_test(self):
    #     pass

    # def third_test(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
