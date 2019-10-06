#! /usr/bin/python
#
# Homework No.  07
# Project No.   01
# File Name:    hw7project1.py
# Programmer:   Karina Elias
# Date:         Oct 06, 2019
#
# Problem Statement:
#   This program will calculate and print the class letter
#   grade given the percentage from the user.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user for percentage
# 3. Use if-else statements to check grade
# 4. Display the letter grade
#
#
# import the necessary python libraries
# for this program none are needed


def main():
    # Print introduction
    print("This program will display the letter grade given"
          " the percentage.\n")

    # ---INPUT--- #
    percentage = eval(input("Enter percentage: "))

    # ---PROCESS--- #
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # ---OUTPUT--- #
    print("Letter grade:", grade)


main()
