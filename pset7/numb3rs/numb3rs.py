import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    # check char type
    ip = ip.strip()
    if re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):

        # split number
        ip = ip.split(".")

        # check numbers
        for i in ip:
            if 0 <= int(i) <= 255:
                continue
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()