# wordlength.py

def main():
    print("This program determines the average word length in a sentence "
          "inputted by the user.")
    sentence = input("Enter a sentence: ")
    words = sentence.split(" ")
    total = 0
    for ch in sentence:
        if ch.isalpha():
            total += 1
    length = total / len(words)
    print("The average word length is:", length)


if __name__ == '__main__':
    main()
