# readfile.py
from squareeach import square_each
from sumlist import sum_list
from tonumbers import to_numbers


def main():
    print("This program reads numbers from a file and prints out the sum of "
          "their squares")
    file_name = input("Enter a filename: ")
    file = open(file_name, 'r')
    lines = file.readlines()
    strings = []
    for line in lines:
        split = line.split()
        for num in split:
            strings.append(num)
    nums = to_numbers(strings)
    squares = square_each(nums)
    result = sum_list(squares)
    print("The sum of the squares of the numbers is", result)


if __name__ == '__main__':
    main()
