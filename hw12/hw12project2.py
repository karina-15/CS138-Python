#! /usr/bin/python
#
# Homework No.  12
# Project No.   02
# File Name:    hw12project2.py
# Programmer:   Karina Elias
# Date:         Dec. 12, 2019
#
# Problem Statement:
#   A palindrome is a sentence that contains the same sequence
#   of letters reading it either forwards or backwards. A classic
#   example is: "Able was I, ere I saw Elba." Write a recursive
#   function that detects whether a string is a palindrome.
#   The basic idea is to check that the first and last letters
#   of the string are the same letter; if they are, then the
#   entire string is a palindrome if everything between those
#   letters is a palindrome. There a couple of special cases
#   to check for. If either the first or last character of
#   the string is not a letter, you can check to see if the
#   rest of the string is a palindrome with that character
#   removed. Also, when you compare letters, make sure that
#   you do it in a case-insensitive way.
#
#   Use your function in a program that prompts a user for
#   a phrase and then tells whether or not it is a palindrome.
#   Here's another classic for testing:
#   "A man, a plan, a canal, Panama!"
#
#
# Overall Plan:
# 1. Print introduction
# 2. Ask user for input text
# 3. Remove all non-alphabetic characters and make lowercase
# 4. Check if input text is palindrome using recursion
#       remove the 1st and last character from string each
#       each time it is checked. Base case is when 1 or 0
#       characters are left in the string
# 5. Display if user input string is a palindrome or not
#
#
# import the necessary python libraries and classes
# for this program re is used to remove non-alphabetic chars
import re


# ---FUNCTIONS---
def printIntro():
    print("\nThis program will check if a string is a palindrome.\n")

# make all lowercase and remove non-alphabetic characters
def cleanString(palindrome):
    return re.sub("[^a-zA-Z]+", '', palindrome).lower()

def recursion(cleanString):
    # base case
    # exit recursion after last 2 char are compared
    if len(cleanString) < 2:
        return True
    # 1st and last char in current string are the same
    elif cleanString[0] == cleanString[-1]:
        return recursion(cleanString[1:-1])
    else:
        return False

# ---MAIN---
def main():
    printIntro()

    # ---INPUT---
    text = input("Enter text: ")

    # ---OUTPUT---
    # checks if user input is a palindrome using recursion
    if recursion(cleanString(text)):
        print("'{0}' is a palindrome".format(text))
    else:
        print("'{0}' is not a palindrome".format(text))


if __name__ == '__main__':
    main()
