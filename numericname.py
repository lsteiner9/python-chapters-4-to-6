# numericname.py

def main():
    print("This program determines the numeric value of a name.")
    name = input("Enter a name: ").lower().replace(" ", "")
    sums = 0
    for ch in name:
        sums += ord(ch) - 96
    print("The value is", sums)


if __name__ == '__main__':
    main()
