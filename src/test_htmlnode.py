import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node1 = HTMLNode("<p>")
        return node1

    # def test_not_eq(self):
    #     pass

    # def test_eq_url_none(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
