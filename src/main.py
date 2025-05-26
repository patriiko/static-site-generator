from textnode import TextNode, TextType

def main():
    # Testing
    text = TextNode("Ovo je kod", TextType.LINK, "https://www.boot.dev")
    text1 = TextNode("Ovo je kod", TextType.IMAGE, "https://www.boot.dev")
    print(text)
    print(TextNode.__eq__(text, text1))

if __name__ == "__main__":
    main()