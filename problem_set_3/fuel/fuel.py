def main():
    fraction = get_fraction("Fraction: ")
    fraction = show_fuel(fraction)


def get_fraction(prompt):
    while True:
        try:
            x , y = input(prompt).split("/")
            x , y = int(x), int(y)

            percent = x/y
            if percent <= 1:
                return percent

        except (ValueError, ZeroDivisionError):
            pass

def show_fuel(x):
    while True:
        x = x * 100
        x = round(x)
        try:
            if x <= 1:
                return print("E")
            elif x >= 99:
                return print("F")
            else:
                return print(f"{x}%")
        except (ValueError, ZeroDivisionError):
            pass

main()

