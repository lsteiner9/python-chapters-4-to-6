# sumlist.py

def sum_list(nums):
    count = 0
    for num in nums:
        count += num
    return count


def main():
    print("This program sums all numbers of a list.")
    num = int(input("How many numbers are in your list? "))
    nums = []
    for i in range(num):
        nums.append(int(input("Enter a number: ")))
    print("The original list is:", nums, "and the sum is", sum_list(nums))


if __name__ == '__main__':
    main()
