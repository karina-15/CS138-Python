#! /usr/bin/python
# Homework No.  02
# Project No.   01
# File Name:    hw2project1.py
# Programmer:   Karina Elias
# Date:         Aug. 31, 2019
#
# Problem Statement: Programming Exercise #1 p.53
# Print an introduction that tells the user what
# the program does. Modify the convert.py program (Section 2.2) to
# print an introduction.
#
# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell
#
#
# Overall Plan:
# 1. Print statement for introduction describing program
# 2. Copy convert.py
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print introduction
    print("This program converts the temperature from Celsius")
    print("to Fahrenheit.")

    # Program convert.py (Section 2.2 p.30)
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()
