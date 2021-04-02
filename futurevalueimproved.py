# futurevalueimproved.py

def main():
    print("This program calculates the future value of an investment.")
    value = float(input("Enter the investment amount: "))
    rate = float(input("Enter the annualized interest rate: "))
    years = int(input("Enter the number of years: "))
    print("Year    Value")
    print("-" * 14)
    print("%2d    $%0.2f" % (0, value))
    for i in range(years):
        value = value * (1 + rate)
        print("%2d    $%0.2f" % (i + 1, value))


if __name__ == '__main__':
    main()
