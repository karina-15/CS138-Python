#! /usr/bin/python
#
# Homework No.  05
# Project No.   02
# File Name:    hw5project2.py, input.txt, output.txt
# Programmer:   Karina Elias
# Date:         Sep. 22, 2019
#
# Problem Statement:
#   This program will open a previously saved file (input.txt)
#   containing a total of 20 int, 2 int per lines, separated
#   by a whitespace. It will then read the file, add the 2 ints
#   in ea. line & write the sum to a file (output.txt)
#
#
# Overall Plan:
# 1. Print introduction
# 2. Get file names
# 3. Open input.txt file as read
# 4. Open output.txt file as write
# 5. Create list
# 6. Place ea. line from input.txt file into list
# 7. Split ea. no. to strings
# 8. Convert string to int
# 9. Add numbers
# 10. Write sum to output.txt file
# 11. Close both files
# 12. Display message that sum was saved to output.txt file
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print introduction
    print("\nThis program will take numbers from previously created"
          "\ninput.txt file and write the sums to output.txt file.\n")

    # ---INPUT--- #
    # Get file names
    infileName = "input.txt"
    outfileName = "output.txt"

    # Open files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # ---PROCESS--- #
    # create list to put ea. line substring in
    numberString = []
    index = 0  # used to get 1st & 2nd number as substrings
               # of ea. line in list
    # for loop to process each line in file
    for line in infile:
        # puts ea. line into end of numberString list as a string
        numberString.append(line)
        # splits ea. number in ea. line to 2 substrings, num1 & num2
        num1, num2 = numberString[index].split()
        # converts numbers to strings & calculates sum
        result = int(num1) + int(num2)
        # prints result string to output.txt file
        # using format {:width} 3 & 4 so it's display is clean
        print("{0:3} + {1:3} = {2:4}".format(num1, num2, result),
              file=outfile)
        # increment index to get both numbers in next line of file
        index = index + 1

    # ---OUTPUT--- #
    # Close files
    infile.close()
    outfile.close()

    print("Results were saved to output.txt file.")


main()
