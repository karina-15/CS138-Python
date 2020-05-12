#! /usr/bin/python
#
# Homework No.  05
# Project No.   01
# File Name:    hw5project1.py
# Programmer:   Karina Elias
# Date:         Sep. 20, 2019
#
# Problem Statement: Programming Exercise #4 p.162
#   This program will allow the user to type in a phrase and
#   then outputs the capitalized acronym for that phrase.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user for a phrase
# 3. Split user input string
# 4. Get 1st char of ea. word
# 5. Display acronym using toUpper()
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print introduction
    print("This program will create an acronym for a phrase.")

    # ---INPUT--- #
    phrase = input("Enter a phrase: ")

    # ---PROCESS--- #
    # create an empty list to store ea. substring of phrase
    acronym = []
    # for loop to split phrase string by whitespace into substrings
    for firstLetter in phrase.split():
        # gets 1st letter of ea. substring (word), capitalizes
        # and adds (appends) it to end of acronym list
        acronym.append(firstLetter[0].upper())

    # ---OUTPUT--- #
    # Display acronym
    # using string format and .join to print list as string
    print("Phrase acronym: {0}".format("".join(acronym)))


main()
