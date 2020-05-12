#! /usr/bin/py
#
# Homework No.  07
# Project No.   03
# File Name:    hw7project3.py
# Programmer:   Karina Elias
# Date:         Oct 06, 2019
#
# Problem Statement: Programming Exercise #6 p.230
#   This program will accept a speed limit and a clocked
#   speed and will either print a fine for an illegal speed
#   or a message indicating the speed was legal.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user for speed limit and clocked speed
# 3. Calculate fine
#       If speed is over limit, fine = $50 + ((speed-limit)*5)
#       If speed is over 90mph, fine = fine + $200
# 4. If speed is legal print message
# 5. Display message and fine if applicable
#
#
# import the necessary python libraries
# for this program none are needed


def main():
    # Print introduction
    print("\nThis program will calculate the fine for a speeding ticket"
          "\nor display a message if the speed is legal.\n")

    # ---INPUT--- #
    limit = eval(input("Enter speed limit:   "))
    speed = eval(input("Enter clocked speed: "))
    print()

    # ---PROCESS/OUTPUT--- #
    if speed > limit:
        print("Speed is illegal.")
        fine = (speed - limit) * 5 + 50
        if speed > 90:
            fine += 200
        print("Fine = ${0}".format(fine))
    else:
        print("Speed is legal.")


main()
