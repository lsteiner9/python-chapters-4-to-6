# sqrt.py
from math import sqrt


def next_guess(guess, x):
    return (guess + (x / guess)) / 2


def main():
    print("This program uses Newton's method to approximate a square root.")
    x = int(input("Enter the number to find the square root of: "))
    num = int(input("Enter the number of times to improve the guess: "))
    guess = x/2
    for i in range (num):
        guess = next_guess(guess, x)
    print("The approximation of the square root of", x, "is", guess)
    print("The difference between the approximation and the actual root is",
          abs(sqrt(x) - guess))


if __name__ == '__main__':
    main()
