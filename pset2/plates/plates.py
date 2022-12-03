def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # check min, max, and charecter type
    if len(s) < 2 or len(s) > 6 or not s.isalnum():
        return False

    else:
        for i in range(len(s)):

            # check first two
            if i <= 1 and not s[i].isalpha():
                return False

            # find number after first two
            elif s[i].isnumeric():

                # check first number is 0 and the rest is number
                if s[i] == "0" or not s[i:].isnumeric():
                    return False
                else:
                    break
    return True


main()