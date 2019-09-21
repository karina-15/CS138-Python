#! /usr/bin/python
#
# numbers2text.py - pg.137
#   A program to convert a sequence of Unicode numbers into
#       a string of text.


def main():
    print("This program converts a sequence of Unicode numbers into"
          "\nthe string of text that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr)  # convert digits string to a number
        message = message + chr(codeNum)  # concatenate character to message

    print("\nThe decoded message is:", message)


main()
