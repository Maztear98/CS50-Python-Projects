import inflect

p = inflect.engine()

namelist = []

while True:
    try:
        name = input(str("Name: ").title())
        namelist.append(name)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(namelist)}")


