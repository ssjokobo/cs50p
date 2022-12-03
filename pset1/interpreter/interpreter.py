# input
x, y, z = input("Expression: ").split(" ")
x = float(x)
z = float(z)

# execution
if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/":
    print(f"{x / z:.1f}")