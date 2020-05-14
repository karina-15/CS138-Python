#! /usr/bin/python
# Homework No.  02
# Project No.   02
# File Name:    hw2project2.py
# Programmer:   Karina Elias
# Date:         Aug. 31, 2019
#
# Problem Statement: Programming Exercise #8 p.54
# Write a program that converts degrees Fahrenheit to
# Celsius using the following formula:
# degreesC = 5(degreesF - 32)/9
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user to enter a temperature in degrees Fahrenheit
# 3. Compute conversion from Fahrenheit to Celsius using formula
# 4. Display degrees Fahrenheit entered and degrees in Celsius
#    computed
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print introduction
    print("\nThis program converts the temperature from\n"
          "Fahrenheit to Celsius.\n")

    # Input
    fahrenheit = eval(input("Enter a temperature in degrees Fahrenheit: "))

    # Process
    celsius = 5*(fahrenheit - 32)/9

    # Output
    print(fahrenheit, "degrees Fahrenheit =", round(celsius, 1), "degrees Celsius")


main()
