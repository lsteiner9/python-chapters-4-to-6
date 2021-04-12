# squareeach.py

def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    return nums


def main():
    print("This program squares all numbers of a list.")
    num = int(input("How many numbers are in your list? "))
    nums = []
    for i in range(num):
        nums.append(int(input("Enter a number: ")))
    print("The original list is:", nums)
    print("The squared list is:", square_each(nums))


if __name__ == '__main__':
    main()
