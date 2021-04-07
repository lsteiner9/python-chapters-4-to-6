# sums.py


def sum_n(n):
    count = 0
    for i in range(1, n + 1):
        count += i
    return count


def sum_n_cubes(n):
    count = 0
    for i in range(1, n + 1):
        count += (i * i * i)
    return count


def main():
    print("This program returns sums: of the first n natural numbers and of "
          "the cubes of the first n natural numbers.")
    n = int(input("Enter n: "))
    print("The sum of the first", n, "natural numbers is", sum_n(n))
    print("The sum of the cubes of the first", n, "natural numbers is",
          sum_n_cubes(n))


if __name__ == '__main__':
    main()