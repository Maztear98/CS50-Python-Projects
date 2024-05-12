import random


def main():
    l = get_level()
    gen_int(l)


def get_level():
    while True:
        Level = input("Level: ")
        if Level not in ["1", "2", "3"]:
            continue
        return Level

def gen_int(Level):
    score = 0
    for i in range(10):
        trails = 1
        if Level == "1":
            x = random.randint(0,9)
            y = random.randint(0,9)
        if Level == "2":
            x = random.randint(10,99)
            y = random.randint(10,99)
        if Level == "3":
            x = random.randint(100,999)
            y = random.randint(100,999)

        while True:
            print(f"{x} + {y} = ", end="")
            answer = input()
            if answer == str(x + y):
                score += 1
                break
            elif answer != str(x + y) and trails != 3:
                print("EEE")
                trails += 1
                continue
            else:
                print(f"{x} + {y} = {x + y}")
                break
    print(score)

if __name__ == "__main__":
    main()
