# numbers2text.py

import string


def main():
    print("This program converts a sequence of AsCII numbers into the string of text that it represents.\n")
    inString = input("Please enter the ASCII-encoded message: ")
    msgList = []
    for numStr in inString.split():
        asciiNum = eval(numStr)
        msgList.append(chr(asciiNum))
    message = ""
    print("The decoded message is:", message.join(msgList))


main()
