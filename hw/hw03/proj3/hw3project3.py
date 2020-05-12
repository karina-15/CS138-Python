#! /usr/bin/python
# Homework No.  03
# Project No.   03
# File Name:    hw3project3.py
# Programmer:   Karina Elias
# Date:         Sep. 07, 2019
#
# Problem Statement: Programming Exercise #10 p.77
# Write a program to determine the length of a ladder
# required to reach a given height when leaned against
# a house.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user to enter the height
# 3. Prompt user to enter the angle of the ladder in
#    in degrees
# 4. Convert the angle to radians
#    (use radians = (pi/180)degrees)
# 5. Calculate the length
#    (use length = height / sin(angle))
# 6. Display the resulting length of ladder needed
#
#
# import the necessary python libraries
import math  # Makes the math library available for pi & sin


def main():
    print()
    # Print introduction
    print("This program will calculate the length of a")
    print("ladder required to reach a given height when")
    print("leaned against a house.")
    print()

    # ---Input--- #
    # Get the height
    height = eval(input("Enter the height: "))
    # Get the angle
    angle_degrees = eval(input("Enter the angle of the ladder in degrees: "))
    print()

    # ---Process--- #
    angle_radians = (math.pi / 180) * angle_degrees
    length = height / math.sin(angle_radians)

    # ---Output--- #
    print("The length of the ladder required = %.3f" % length)


main()
