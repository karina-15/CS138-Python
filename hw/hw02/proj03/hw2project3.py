#! /usr/bin/python
# Homework No.  02
# Project No.   03
# File Name:    hw2project3.py
# Programmer:   Karina Elias
# Date:         Aug. 31, 2019
#
# Problem Statement: Programming Exercise #2 p.53
# Modify avg2.py program (Section 2.5.3 p.42) to find the
# average of N (where N is any number) exam scores.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user to enter the total number of scores that they
#    will enter
# 3. Use a for loop to add up all the scores entered by user
# 4. Divide the sum from step 3 by total number of scores user
#    entered in step 2
# 5. Display average exam score
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print introduction
    print("This program will calculate the average for any number")
    print("of exam scores entered.")

    # Input
    # Get total number of exam scores that will be entered
    num_exams = eval(input("Enter the number of exam scores to be averaged: "))
    # Initialize sum_total to 0
    sum_total = 0
    # Use for loop to enter each exam score
    # num starts at 0, so +1 to start print at 1
    for num in range(num_exams):
        print("Enter Exam Score {}:".format(num+1), end=" ")
        sum_total = sum_total + eval(input())
    # End of for loop
    print()

    # Process
    # Calculate the average
    avg = sum_total/num_exams

    # Output
    # Display the average
    print("Average Exam Score:", round(avg))


main()
