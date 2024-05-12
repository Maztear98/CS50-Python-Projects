expression = input("Expresion: ").split(" ")
x, y, z = expression

a = float(x)
b = float(z)

if y == "+":
    print(f"{a + b:.1f}")
elif y == "-":
    print(f"{a - b:.1f}")
elif y == "*":
    print(f"{a * b:.1f}")
else:
    print(f"{a / b:.1f}")
