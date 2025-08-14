from htmlnode import LeafNode


def main():
    textnode = LeafNode("p", "hello")
    print(textnode.to_html())


if __name__ == "__main__":
    main()
