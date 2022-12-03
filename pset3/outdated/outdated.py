# months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# main
def main():
    while True:

        # input
        date = input("Date: ")

        # first format
        try:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            if valid_day(d) and valid_month(m):
                print(f"{y}-{m:02d}-{d:02d}")
                break
        except ValueError:

            # second format
            try:
                m, d, y = date.split(" ")
                m = months.index(m) + 1
                d = int(d[:-1])
                if valid_day(d):
                    print(f"{y}-{m:02d}-{d:02d}")
                    break
            except ValueError:
                pass


# check possible days
def valid_day(day):
    if 1 <= day <= 31:
        return True
    else:
        return False


# check possible months
def valid_month(month):
    if 1 <= month <= 12:
        return True
    else:
        return False


main()