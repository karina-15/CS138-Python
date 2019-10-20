#! /usr/bin/python
#
# Homework No.  08
# Project No.   01
# File Name:    hw8project1.py
# Programmer:   Karina Elias
# Date:         Oct 20, 2019
#
# Problem Statement: Programming Exercise #1 p.262
#    Write a program that computes and outputs the nth Fibonacci number,
#    where n is a value entered by the user.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user for number
# 3. Use recursive function to get Fibonacci number
#       sum of previous 2 numbers
#       fib(n - 1) + fib(n - 2)
# 4. Display the nth Fibonacci number
#
#
# import the necessary python libraries
# for this program none are needed

# ---PROCESS--- #
# Fibonacci number is solved recursively (calls itself)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    # Print introduction
    print("This program will display the Fibonacci number for nth term.\n")

    # ---INPUT--- #
    n = eval(input("Enter a positive number: "))

    # ---OUTPUT--- #
    if n >= 0:
        print("Fibonacci number for term {0}: {1}".format(n, fib(n)))
    else:
        print("{0} is not a valid number.".format(n))


main()
