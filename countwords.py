# countwords.py

def main():
    print("This program counts the number of words in an inputted sentence.")
    sentence = input("Enter a sentence: ")
    count = 0
    alpha_flag = False
    for ch in sentence:
        if ch == " " and alpha_flag:
            count += 1
            alpha_flag = False
        elif ch != " ":
            alpha_flag = True
    if alpha_flag:
        count += 1

    print("There are", count, "words in this sentence.")


if __name__ == '__main__':
    main()
