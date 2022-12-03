from datetime import date
import math
import time
import sys
import inflect


p = inflect.engine()


def main():
    try:
        # input and format date
        birthday = input("Date of Birth: ")

        # get the age
        age = get_age_minutes(birthday)

        # convert to word
        age = p.number_to_words(age).capitalize().split(" and ")

        # print
        for i in age:
            print(i, end=" ")
        print("minutes")

    # handling input format
    except ValueError:
        sys.exit("Invalid date")


def get_age_minutes(birthday):
    # formating
    y, m, d = birthday.split("-")

    # age calculation
    birthday = date(int(y), int(m), int(d))
    today = date.today()
    age = today - birthday
    age = age.days
    return age * 24 * 60


if __name__ == "__main__":
    main()