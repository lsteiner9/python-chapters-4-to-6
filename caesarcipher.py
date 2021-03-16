# caesarcipher.py

def main():
    print("This program encodes and decodes a Caesar cipher.")
    phrase = input("Enter a phrase to encode: ")
    key = int(input("Enter a key value: "))
    encoded = []
    for ch in phrase:
        encoded.append(chr(ord(ch) + key))
    message = ""
    print("The encoded message is:", message.join(encoded))

    phrase = input("Enter a phrase to decode: ")
    key = int(input("Enter a key value: "))
    decoded = []
    for ch in phrase:
        decoded.append(chr(ord(ch) - key))
    message = ""
    print("The decoded message is:", message.join(decoded))


if __name__ == '__main__':
    main()
