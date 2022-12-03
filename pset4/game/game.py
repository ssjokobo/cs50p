# import module
import random

# get level
while True:
    try:
        level = int(input("Level: "))
        if 1 <= level <= 100:
            break
    except ValueError:
        pass

# randomize a number
num = random.randrange(1, level + 1)

# guess and check
while True:
    try:
        guess = int(input("Guess: "))
        if 1 <= guess <= 100:
            if guess < num:
                print("Too small!")
            elif guess > num:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass