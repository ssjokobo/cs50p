def main():

    # input
    answer = input("Greeting: ")
    cash = value(answer)
    print(f"${cash}")


def value(greeting):

    # formatting
    greeting = greeting.lower().strip()

    # execution
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()