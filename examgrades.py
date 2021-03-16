# examgrades.py

def main():
    print("This program converts from a number grade to a letter grade.")
    grade = int(input("Enter a number grade: "))
    if grade >= 90:
        letterGrade = "A"
    elif grade >= 80:
        letterGrade = "B"
    elif grade >= 70:
        letterGrade = "C"
    elif grade >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"

    print("The grade is", letterGrade)


if __name__ == '__main__':
    main()
