import sys
import os
from PIL import Image, ImageOps


# main
def main():

    # supported extensions
    ext = [".jpg", ".jpeg", ".png"]

    # check argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        ext_1 = os.path.splitext(sys.argv[1])[1]
        ext_2 = os.path.splitext(sys.argv[2])[1]
        if ext_1 not in ext or ext_2 not in ext:
            sys.exit("Invalid input")
        elif ext_1 != ext_2:
            sys.exit("Input and output have different extensions")

    # execute
    try:
        wear_it(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


def wear_it(input, output):

    # open files
    photo = Image.open(input)
    shirt = Image.open("shirt.png")

    # size
    size = shirt.size

    # resize
    photo = ImageOps.fit(photo, size)

    # wear the shirt
    photo.paste(shirt, shirt)

    # save into a new file
    photo.save(output)


if __name__ == "__main__":
    main()