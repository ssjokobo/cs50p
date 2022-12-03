def main():
    # input
    text = input("Input: ")

    # shorten
    shorten_text = shorten(text)

    # print
    print("Output: " + shorten_text)

    # adjust line
    print()


def shorten(word):
    # const
    vowels = ["a", "e", "i", "o", "u"]

    # string
    short_form = ""

    # check for vowels
    for char in word:
        if char.lower() not in vowels:
            short_form += char

    return short_form


if __name__ == "__main__":
    main()