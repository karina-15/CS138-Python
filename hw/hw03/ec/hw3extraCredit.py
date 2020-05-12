#! /usr/bin/python
# Homework No.  03
# Extra Credit
# File Name:    hw3extraCredit.py
# Programmer:   Karina Elias
# Date:         Sep. 07, 2019
#
# Problem Statement: Programming Exercise #8 p.77
# Find the Gregorian epact (# of days b/w Jan. 1st
# and prev. new moon) given a 4-digit year
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user to a year
# 3. Validate 4 digit year was entered with while loop
#       while year<1000 or year>9999:
# 4. Calculate variable C (use C=year//100)
# 5. Calculate the epact
#    (use epact = (8+(C//4)-C+((8C+13)//25)+11(year%19))%30
# 6. Display the epact number
#
#
# import the necessary python libraries
# for this program none are needed


def main():
    print()
    # Print introduction
    print("This program will calculate the epact number")
    print("given a 4-digit year.")
    print()

    # ---Input--- #
    # Get the year
    year = eval(input("Enter a year: "))
    # Validate year is 4-digits
    while year < 1000 or year > 9999:
        year = eval(input("Try again. Please enter a year(YYYY): "))
    print()

    # ---Process--- #
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30

    # ---Output--- #
    print("The epact number for the year %d = %d" % (year, epact))


main()
