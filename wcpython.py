# wcpython.py

def main():
    print("This program counts the number of lines, words, and characters in "
          "a file.")
    filename = input("Enter filename: ")
    file = open(filename, 'r')
    lines = file.readlines()
    wordcount = 0
    charcount = 0
    for line in lines:
        charcount += len(line)
        words = line.split(" ")
        wordcount += len(words)
    print("There are", len(lines), "lines,", wordcount, "words, and", charcount,
          "characters in this file.")


if __name__ == '__main__':
    main()