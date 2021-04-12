# acronym.py

def acronym(phrase):
    message = []
    for word in phrase.split():
        message.append(word[0])
    messageStr = ""
    return messageStr.join(message).upper()

def main():
    print("This program creates an acronym based on an inputted phrase.")
    phrase = input("Enter a phrase: ")
    print("The acronym is", acronym(phrase))


if __name__ == '__main__':
    main()
