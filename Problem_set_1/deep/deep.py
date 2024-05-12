# Ask what is the answer to the Great question of life, universe and everything

x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().casefold()

match x:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")


