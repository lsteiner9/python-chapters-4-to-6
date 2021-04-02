# chaosimproved.py

def main():
    print("This program allows the user to input two initial values and a "
          "number of iterations, for a table of results of a chaotic function "
          "on the values.")
    value1 = float(input("Enter a value: "))
    value2 = float(input("Enter another value: "))
    iterations = int(
        input("Enter the number of iterations for the chaotic function: "))
    print("index     {value1}        {value2}".format(value1=value1,
                                                      value2=value2))
    print("-" * 28)
    for i in range(iterations):
        value1 = 3.9 * value1 * (1 - value1)
        value2 = 3.9 * value2 * (1 - value2)
        print("%2d      %7.6f    %7.6f" % (i + 1, value1, value2))


if __name__ == '__main__':
    main()
