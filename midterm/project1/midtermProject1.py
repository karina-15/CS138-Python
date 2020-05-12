#! /usr/bin/python
#
# Homework No.  Midterm
# Project No.   01
# File Name:    midtermProject1.py, numbers.txt
# Programmer:   Karina Elias
# Date:         Oct. 13, 2019
#
# Problem Statement:
#   This program will find the mean, median, and standard
#   deviation of a list of numbers which are read from a file.
#   1 number per line and supports both positive and negative
#   numbers.
#   Mean is defined as the sum of all the given elements
#   divided by the total number of elements.
#   Median is defined as the middle number (in a sorted list
#   of numbers).
#   Standard deviation is a statistical measure of spread or
#   variability. The standard deviation is the root mean square
#   (RMS) deviation of the values from their arithmetic mean.
#   List the 2 standard deviation range.
#   Handle any errors that may occur with lists that vary in
#   size from 0 to 1000.
#   Formula for standard deviation
#       S = sqrt(sum(((score - mean) ** 2) / (n - 1)))
#
#
# Overall Plan:
# 1. Print introduction
# 2. Get file name
# 3. Open numbers.txt file as read
# 4. Create list
# 5. Place ea. line from numbers.txt file into list
# 6. Sort numbers in list
# 7. Create variable to store sum of all numbers in list
# 8. Create variable to store size of list
# 9. Calculate mean
#       mean = sum(numbers) / n
# 10. Calculate median using sort() and getting middle number
#       if list has even numbers get the avg. of the middle
#       2 numbers in the sorted list
# 11. Calculate standard deviation using formula
# 12. Display mean, median, and standard deviation
# 13. Close file
# 14. Handle possible index out of range exceptions (0-1000)
#
#
# import the necessary python libraries
# for this program math is needed
import math


def main():
    # Print introduction
    print("\nThis program will take numbers from previously created"
          "\nnumbers.txt file and display the mean, median, and standard"
          "\ndeviation.\n")

    try:
        # ---INPUT--- #
        # Get file name
        infileName = "numbers.txt"
        # Open file
        infile = open(infileName, "r")

        # ---PROCESS--- #
        # create list to put ea. number/line in
        numbers = []
        # for loop to put ea. number/line in file to list
        for line in infile:
            numbers.append(int(line))   # add each line as a number
        # sort numbers in list by smallest to largest
        numbers.sort()
        # sum of all numbers in list
        listSum = sum(numbers)
        # Exception handling for list with size out of range
        if len(numbers) < 0 or len(numbers) > 1000:
            raise IndexError
        # total of numbers in list
        n = len(numbers)
        if n == 0:   # no numbers in file/list
            raise ZeroDivisionError
        # calculate mean
        mean = listSum / n
        # calculate median (-1 b/c index of list starts at 0)
        if n % 2 == 0:  # if size of list is even
            num1 = numbers[int(n / 2) - 1]
            num2 = numbers[int(n / 2)]
            median = (num1 + num2) / 2
        else:           # if size of list is odd
            median = numbers[int(n / 2)]
        # calculate standard deviation
        sum_stdev = 0.0
        # calculate sum of ea. number under the square root
        for score in numbers:
            sum_stdev += ((score - mean) ** 2) / (n - 1)
        # calculate square root of sum
        s = math.sqrt(sum_stdev)

        # ---OUTPUT--- #
        print("Mean = {0:.3f}\nMedian = {1}\nstandard deviation = {2:.3f}"
              .format(mean, median, s))
        # Close file
        infile.close()

    # Exception Handling
    except IndexError:
        print('Index error: Amount of numbers in file is out of range (0-1000)')
    except ValueError:
        print('Error value: numbers in file must be integers')
    except ZeroDivisionError:
        print('ZeroDivisionError: No numbers in file. Cannot calculate mean.')
    except FileNotFoundError:
        print('\'{0}\' File not found.'.format(infileName))


main()
