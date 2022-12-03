import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # search and extract the address
    if address := re.search("\"http(://|s://|s://www\.)youtube\.com/embed/([a-zA-z0-9]+)\"", s):
        # string format the link for youtu.be
        return "https://youtu.be/" + address.group(2)
    else:
        return None


if __name__ == "__main__":
    main()