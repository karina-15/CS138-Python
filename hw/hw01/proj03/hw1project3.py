#! /usr/bin/python
# Homework No.  01
# Project No.   03
# File Name:    hw1project3.py
# Programmer:   Karina Elias
# Date:         Aug. 25, 2019
#
# Problem Statement:
# Ask the user to enter number of completions made and number of passes
# attempted, compute the completion percentage, and display the percentage
# to the screen.
#
#
# Overall Plan:
# 1. Print initial message to the screen
# 2. Prompt user for number of completions made
# 3. Prompt user for number of pass attempts
# 4. Calculate the percentage of pass completions
# 5. Print the percentage to the screen
#
#
# import the necessary python libraries
# for this program none are needed


def main():
    # Input
    print("This program will calculate the completion percentage for a quarterback.")
    print("Enter number of completions:")
    num1 = eval(input())
    print("Enter number of pass attempts:")
    num2 = eval(input())

    # Process
    percentage = (num1 / num2) * 100

    # Output
    print("Completion percentage =", percentage)


main()
