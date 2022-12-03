# main
def main():
    while True:
        try:
            user_input = input("Fraction: ")
            percent = convert(user_input)
            gauge_read = gauge(percent)
            print(gauge_read)
        except (TypeError, ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    level, full = fraction.split("/")
    level = int(level)
    full = int(full)
    return level / full * 100


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        percentage = round(percentage)
        return f"{percentage}%"


if __name__ == "__main__":
    main()