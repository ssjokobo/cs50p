import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # look for and counting um
    um = re.findall("\Wum\W|^um\W|\Wum$|^um$", s, re.IGNORECASE)
    # return
    return len(list(um))


if __name__ == "__main__":
    main()