#! /usr/bin/python
#
# printfile.py
#   Prints an entire file to the screen.


def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)


main()
