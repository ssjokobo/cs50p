# tracker
grocery = {}

# main
while True:
    try:
        item = input().upper()
        grocery[item] += 1
    except KeyError:
        grocery[item] = 1
    except EOFError:
        for item in sorted(grocery.keys()):
            print(grocery[item], item)
        break