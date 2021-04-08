# fibo.py

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def main():
    print("This program returns the nth Fibonacci number.")
    n = int(input("Enter n: "))
    print("The Fibonacci number at position", n, "is", fibo(n))


if __name__ == '__main__':
    main()
