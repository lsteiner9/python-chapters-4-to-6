# sphere.py

from math import pi


def sphere_area(radius):
    return 4 * pi * (radius * radius)


def sphere_volume(radius):
    return (4 / 3) * pi * (radius * radius * radius)


def main():
    print("This program finds the area and volume of a sphere.")
    radius = float(input("Enter the radius: "))
    print("The area of the sphere is", sphere_area(radius))
    print("The volume of the sphere is", sphere_volume(radius))


if __name__ == '__main__':
    main()