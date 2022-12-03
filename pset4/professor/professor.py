import random


def main():
    # score
    score = 0

    # get level
    level = get_level()

    # loop questions
    for _ in range(10):

        # get question
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y

        # three chances to answer
        counter = 3
        while counter > 0:
            try:
                # get answer
                ans = int(input(f"{x} + {y} = "))

                # check answer
                if ans == z:
                    score += 1
                    break
                else:
                    print("EEE")
                    counter -= 1

            # check for non-integer
            except ValueError:
                pass

        # if fail three times
        if counter == 0:
            print(f"{x} + {y} = {z}")

    # print score
    print(f"score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    else:
        if level == 1:
            return random.randrange(0, 10)
        else:
            return random.randrange(10 ** (level - 1), 10 ** level)


if __name__ == "__main__":
    main()