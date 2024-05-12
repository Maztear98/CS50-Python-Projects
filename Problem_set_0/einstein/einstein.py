# calculate Einstein's theory relativity E=mc2

def main():
    M = int(input("What's the mass in Kgs? M - "))
    C = int("300000000")

    print("Energy E is equal to", M * (square(C)) )

def square(n):
    return n * n

main()
