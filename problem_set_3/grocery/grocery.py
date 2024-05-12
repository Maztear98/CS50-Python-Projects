shopping_list = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    if item in shopping_list:
        shopping_list[item] += 1

    else:
        shopping_list[item] = 1

for item in sorted(shopping_list.keys()):
    print(shopping_list[item], item)

