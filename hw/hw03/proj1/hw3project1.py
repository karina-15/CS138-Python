#! /usr/bin/python
# Homework No.  03
# Project No.   01
# File Name:    hw3project1.py
# Programmer:   Karina Elias
# Date:         Sep. 07, 2019
#
# Problem Statement: Programming Exercise #2 p.76
# Write a program that calculates the cost per square inch of a
# circular pizza, given its diameter and price. The formula for
# area is A=pi*r^2
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user to enter the pizza's diameter in inches
# 3. Prompt user to enter the pizza's price
# 4. Calculate the radius of the pizza (radius = diameter/2)
# 5. Calculate the area of the pizza (A=(pi)*(r**2))
# 6. Calculate cost per square inch (price/A)
# 7. Display cost per square inch
#
#
# import the necessary python libraries
import math  # Makes the math library available for pi


def main():
    # Print introduction
    print("This program will calculate the cost per square"
          " inch of a circular pizza.")

    # ---Input--- #
    # Get the diameter of the pizza in inches
    diameter = eval(input("Enter the diameter of the pizza in"
                          " inches: "))
    # Get the price of the pizza
    price = eval(input("Enter the price of the pizza: $"))

    # ---Process--- #
    radius = diameter / 2
    area = math.pi * radius ** 2
    cost_sq_in = price / area

    # ---Output--- #
    print("Cost = $%.2f/sq.in." % round(cost_sq_in, 2))


main()
