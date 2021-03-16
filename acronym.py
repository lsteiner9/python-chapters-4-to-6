# acronym.py

def main():
    print("This program creates an acronym based on an inputted phrase.")
    phrase = input("Enter a phrase: ")
    message = []
    for word in phrase.split():
        message.append(word[0])
    messageStr = ""
    print("The acronym is", messageStr.join(message).upper())


if __name__ == '__main__':
    main()
