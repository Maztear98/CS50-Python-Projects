

amount = 0
coke_price = 50
denomination = [5,10,25]

while amount < coke_price:
    print(f"Amount Due: {coke_price - amount}")

    user_input = int(input("Insert Coin: "))
    if user_input in denomination:
        amount += user_input

print(f"Change Owed: {amount - coke_price}")
