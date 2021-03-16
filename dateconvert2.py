# dateconvert2.py

import string


def main():
    day = int(input("Please enter day, month, and year numbers: "))
    month = int(input())
    year = int(input())

    date1 = str(month) + "/" + str(day) + "/" + str(year)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    monthStr = months[month - 1]
    date2 = monthStr + "" + str(day) + ", " + str(year)
    print("The date is %d/%d/%d or %s%d%d." % (month, day, year, monthStr, day, year))


main()

