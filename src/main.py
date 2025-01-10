from textnode import TextNode, TextType


def main():
    node = TextNode("First text node", TextType.BOLD, "github.com/haneyeric")
    print(node)


main()
