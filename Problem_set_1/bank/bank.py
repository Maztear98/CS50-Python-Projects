# Bank Greeting set it up in way it checks what the input is written for the greeting

x = input("Greeting: ").strip().casefold()

if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")


