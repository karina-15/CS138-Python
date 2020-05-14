#! /usr/bin/python
# Homework No.  01
# Project No.   01
# File Name:    hw1project1.py
# Programmer:   Karina Elias
# Date:         Aug. 25, 2019
#
# Problem Statement: Ask the user to enter three numbers, calculate the sum of
# these three numbers, calculate the multiplication of these three numbers,
# and display the sum and multiplication to the screen
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for three integers
# 3. Calculate the sum of the integers
# 4. Calculate the multiplication of the integers
# 5. Print the sum and multiplication of the integers to the screen
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("\nHello!")
    print("I can add three numbers for you")

    # Variables are declared dynamically no need to pre-define
    print("Enter one whole numbers(Ex. 52): ")
    num1 = eval(input())
    print("Enter another whole numbers(Ex. 41): ")
    num2 = eval(input())
    print("Enter a third whole number: ")
    num3 = eval(input())

    # Here is the processing that is needed
    sum = num1 + num2 + num3
    result = num1 * num2 * num3

    # Output the results
    print("The sum of the three numbers is", sum)
    print("The result of multiplying the\nthree numbers is", result)


main()
