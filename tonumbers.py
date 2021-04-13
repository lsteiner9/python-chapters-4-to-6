# tonumbers.py

def to_numbers(str_list):
    for i in range(len(str_list)):
        str_list[i] = eval(str_list[i])
    return str_list


def main():
    print(
        "This program takes numerical strings and converts them into numbers.")
    num = int(input("How many numbers are in your list? "))
    nums = []
    for i in range(num):
        nums.append(input("Enter a number: "))
    print("The list is", to_numbers(nums))


if __name__ == '__main__':
    main()