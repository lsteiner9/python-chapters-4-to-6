# countwords.py

def main():
    print("This program counts the number of words in an inputted sentence or "
          "a file.")
    if input("Type 1 to input the sentence, 2 to input a file: ") == "1":
        sentence = input("Enter a sentence: ")
        words = sentence.split(" ")
        print("There are", len(words), "words in this sentence.")
    else:
        filename = input("Enter filename to count words from: ")
        file = open(filename, 'r')
        count = 0
        for line in file.readlines():
            words = line.split(" ")
            count += len(words)
        print("There are", count, "words in this file.")


if __name__ == '__main__':
    main()
