# quizgrades.py

def grade(score):
    grade_dict = {5: "A", 4: "B", 3: "C", 2: "D", 1: "F", 0: "F"}
    return grade_dict[score]


def main():
    print("This program converts from a number grade to a letter grade.")
    score = int(input("Enter a grade number from 0-5: "))
    print("The corresponding letter grade is", grade(score))


if __name__ == '__main__':
    main()