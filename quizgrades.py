# quizgrades.py

def main():
    gradeDict = {5: "A", 4: "B", 3: "C", 2: "D", 1: "F", 0: "F"}
    print("This program converts from a number grade to a letter grade.")
    grade = int(input("Enter a grade number from 0-5: "))
    print("The corresponding letter grade is", gradeDict[grade])


main()
