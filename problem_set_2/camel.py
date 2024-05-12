c = input("camelCase: ")

s = ""

for i in range(len(c)):
    if c[i].isupper():
        s = s + "_" + c[i].lower()
    else:
        s += c[i].lower()

print("snake_case: ", s)



