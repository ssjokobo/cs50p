import sys
import csv


# main
def main():

    # check argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Must be CSV files")
    else:
        try:
            separate_first_last(sys.argv[1], sys.argv[2])
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


# read file and create table
def separate_first_last(input, output):

    # read file
    with open(input) as input_file:
        reader = csv.DictReader(input_file)

        # write file
        with open(output, "w") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            writer.writeheader()

            # loop through rows
            for row in reader:

                # formatting
                last, first = row["name"].split(",")
                new_format = {
                    "first": first.lstrip(),
                    "last": last,
                    "house": row["house"]
                }
                writer.writerow(new_format)


if __name__ == "__main__":
    main()