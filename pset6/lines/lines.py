import sys


# main
def main():

    # check argv
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            counted_lines = read(sys.argv[1])
            print(counted_lines)
        except FileNotFoundError:
            sys.exit("File does not exist")


# read file and count lines
def read(file_name):
    counter = 0

    # read file
    with open(file_name) as file:
        for line in file:
            if line.lstrip() == "":
                pass
            elif line.lstrip().startswith("#"):
                pass
            else:
                counter += 1
    return counter


if __name__ == "__main__":
    main()