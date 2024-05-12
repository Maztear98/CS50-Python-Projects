import random

while True:
    try:
        Level = int(input("Level: "))
    except ValueError:
        continue
    if 0 >= Level:
        continue

    num = random.randint(1, Level)
    break

while True:
    try:
        Guess = int(input("Guess: "))
        if 0 >= Guess:
            continue
    except ValueError:
        continue

    if Guess > num:
        print("Too large!")
    if Guess < num:
        print("Too small!")
    if Guess == num:
        print("Just right!")
        break
