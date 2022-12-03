# input
text = input("camelCase: ")

# formatting response
print("snake_case: ", end="")

# looping letters
for char in text:
    if char.islower():
        print(char, end="")
    else:
        print("_", end="")
        print(char.lower(), end="")

# adjusting line
print()