# change2.py

def main():
    print("Change Counter\nPlease enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = quarters * 25 + dimes * 10 + nickles * 5 + pennies
    print("\nThe total value of your change is $%d.%02d" % (total/100, total%100))


main()
