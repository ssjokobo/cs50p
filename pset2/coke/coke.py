# const
valid_coins = [5, 10, 25]

# price
due = 50

# loop
while True:
    print("Amount Due:", str(due))
    coin = int(input("Insert Coin: "))

    # check coin type and deduct
    if coin in valid_coins:
        due -= coin

    # check if fully paid
    if due <= 0:
        print("Change Owed:", str(abs(due)))
        break