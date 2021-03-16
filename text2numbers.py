# text2numbers.py

def main():
    print("This program converst a textual message into a sequence of numbers representing the ASCII encoding of the "
          "message.")
    message = input("Please enter the message to encode: ")
    print()
    print("Here are the ASCII codes:")
    for ch in message:
        print(ord(ch),)

    print()


main()
