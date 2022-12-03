import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # searching for matches
    if hours := re.search("^([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([0-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$", s):

        # handling start hour
        if hours.group(3) == "AM":
            start_hour = int(hours.group(1))
            if start_hour == 12:
                start_hour = 0
        elif hours.group(3) == "PM":
            start_hour = int(hours.group(1)) + 12
            if start_hour == 24:
                start_hour = 12

        # handling stop hour
        if hours.group(6) == "AM":
            stop_hour = int(hours.group(4))
            if stop_hour == 12:
                stop_hour = 0
        elif hours.group(6) == "PM":
            stop_hour = int(hours.group(4)) + 12
            if stop_hour == 24:
                stop_hour = 12

        # handling start minute
        try:
            start_min = hours.group(2)[1:]
        except TypeError:
            start_min = "00"

        # handling stop minute
        try:
            stop_min = hours.group(5)[1:]
        except TypeError:
            stop_min = "00"

        # return
        return f"{start_hour:02d}:{start_min} to {stop_hour:02d}:{stop_min}"

    else:
        raise(ValueError)


if __name__ == "__main__":
    main()