# input
answer = input("Greeting: ").lower().strip()

# execution
if answer.startswith("hello"):
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")