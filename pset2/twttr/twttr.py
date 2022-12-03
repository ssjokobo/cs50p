# const
vowels = ["a", "e", "i", "o", "u"]

# input
text = input("Input: ")

# check for vowels
for char in text:
    if char.lower() not in vowels:
        print(char, end="")

# adjust line
print()