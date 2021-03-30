# caesarcipher.py

def main():
    print("This program encodes and decodes a Caesar cipher.")
    phrase = input("Enter a phrase to encode: ")
    key = int(input("Enter a key value: "))
    encoded = []
    for ch in phrase:
        number = ord(ch)
        if not chr(number).isspace():
            if not chr(number + key).isalpha():
                number -= 58
            number += key
        encoded.append(chr(number))
    message = ""
    print("The encoded message is:", message.join(encoded))

    phrase = input("Enter a phrase to decode: ")
    key = int(input("Enter a key value: "))
    decoded = []
    for ch in phrase:
        number = ord(ch)
        if not chr(number).isspace():
            if not chr(number - key).isalpha():
                number += 58
            number -= key
        decoded.append(chr(number))
    message = ""
    print("The decoded message is:", message.join(decoded))


if __name__ == '__main__':
    main()
