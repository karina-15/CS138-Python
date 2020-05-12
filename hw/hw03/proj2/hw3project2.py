#! /usr/bin/python
# Homework No.  03
# Project No.   02
# File Name:    hw3project2.py
# Programmer:   Karina Elias
# Date:         Sep. 07, 2019
#
# Problem Statement:
# Write a program that divides 2 numbers and outputs the
# results using whole numbers and the remainder.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user to enter a number for the numerator
# 3. Prompt user to enter a number for the denominator
# 4. If denominator equals zero, prompt user for another number
# 5. Calculate the division's whole number (use // for integers)
# 6. Calculate the division's remainder (use %)
# 7. Display the resulting whole number and remainder
#
#
# import the necessary python libraries
# for this program none are needed


def main():
    print()
    # Print introduction
    print("This program will divide 2 numbers and display the")
    print("answer with whole numbers and the remainder.")
    print()

    # ---Input--- #
    # Get the numerator
    numerator = eval(input("Enter a number for the numerator: "))
    # Get the denominator
    denominator = eval(input("Enter a number for the denominator: "))
    while denominator == 0:
        denominator = eval(input("Try again. Enter a number other than 0: "))
    print()

    # ---Process--- #
    whole_number = numerator // denominator
    remainder = numerator % denominator

    # ---Output--- #
    print("%d/%d = %dR%d" % (numerator, denominator, whole_number, remainder))


main()
