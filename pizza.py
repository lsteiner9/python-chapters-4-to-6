# pizza.py
from math import pi


def pizza_area(diameter):
    radius = diameter / 2
    return 4 * pi * radius * radius


def pizza_price(area, cost):
    return cost / area


def main():
    print("This program returns the price per square inch of a pizza.")
    diameter = float(input("Enter the diameter: "))
    cost = float(input("Enter the price: "))
    print("This pizza costs", pizza_price(pizza_area(diameter), cost),
          "per square inch.")


if __name__ == '__main__':
    main()
