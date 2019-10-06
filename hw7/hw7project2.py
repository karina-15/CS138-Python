#! /usr/bin/python
#
# Homework No.  07
# Project No.   02
# File Name:    hw7project2.py
# Programmer:   Karina Elias
# Date:         Oct 06, 2019
#
# Problem Statement:
#   This program will estimate the adult height of a child
#   using the formulas below and the height of the parents.
#   All input heights are in inches and output in feet and inches.
#   Formulas:
#   maleHeight = ((motherHeight * 13 / 12) + fatherHeight) / 2
#   femaleHeight = ((fatherHeight * 12 / 13) + motherHeight) / 2
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user child's gender, mother's height, and father's height
# 3. Calculate estimated height using matching formula
# 4. Display height in inches converted to feet and inches
#
#
# import the necessary python libraries
# for this program none are needed


def main():
    # Print introduction
    print("\nThis program will display the estimated adult height"
          " of a child.\n")

    # ---INPUT--- #
    gender = input("Enter child's gender: ")
    gender = gender[0].lower()

    while gender != 'm' and gender != 'b' and gender != 'f' and gender != 'g':
        gender = input("Invalid entry for gender."
                       "\nPlease enter male or female: ")
        gender = gender[0].lower()

    momH = eval(input("Enter mother's height (in inches): "))
    dadH = eval(input("Enter father's height (in inches): "))

    # ---PROCESS--- #
    if gender == 'm' or gender == 'b':
        adultH = ((momH * (13 / 12)) + dadH) / 2
    else:
        adultH = ((dadH * (12 / 13)) + momH) / 2

    # calculate height from inches to feet and inches
    feet = adultH / 12
    inches = round(adultH % 12)

    # ---OUTPUT--- #
    print("\nChild's adult height: {2:.2f} inches = {0}'{1}\""
          .format(int(feet), int(inches), adultH))


main()
