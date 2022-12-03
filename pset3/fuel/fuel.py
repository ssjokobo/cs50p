# input
def get_fuel():
    return input("Fraction: ").split("/")


# calculate
def get_percent(level, full):
    return level / full * 100


# print
def print_percent(percent):
    if percent < 1:
        print("E")
    elif percent > 99:
        print("F")
    else:
        percent = round(percent)
        print(f"{percent}%")


# main
def main():
    while True:
        try:
            level, full = get_fuel()
            level = int(level)
            full = int(full)
            if level > full:
                pass
            else:
                percent = get_percent(level, full)
                print_percent(percent)
                break
        except (TypeError, ValueError, ZeroDivisionError):
            pass


main()