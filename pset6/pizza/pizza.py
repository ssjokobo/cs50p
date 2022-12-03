import sys
import csv
from tabulate import tabulate


# main
def main():

    # check argv
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            table = create_table(sys.argv[1])
            headers = table[0]
            print(tabulate(table[1:], headers, tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")


# read file and create table
def create_table(file_name):
    table = []

    # read file
    with open(file_name) as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            table.append([])
            for item in row:
                table[i].append(item)
    return table


if __name__ == "__main__":
    main()