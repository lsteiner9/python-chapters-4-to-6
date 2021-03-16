# userfile.py

import string


def main():
    print("This program creates a file of usernames from a file of names.")
    infilename = input("What file are the names in? ")
    outfilename = input("What file should the usernames go in? ")
    infile = open(infilename, 'r')
    outfile = open(outfilename, 'w')
    for line in infile:
        first, last = line.split()
        uname = string.ascii_lowercase(first[0] + last[:7])
        outfile.write(uname + '\n')

    infile.close()
    outfile.close()

    print("Usernames have been written to", outfilename)


main()
