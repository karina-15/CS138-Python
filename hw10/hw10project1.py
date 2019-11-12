#! /usr/bin/python
#
# Homework No.  10
# Project No.   01
# File Name:    hw10project1.py
# Programmer:   Karina Elias
# Date:         Nov. 11, 2019
#
# Problem Statement:
#   This program will count the reserved words in a python file.
#   Uses reserved.txt file for reserved word list from p.469.
#   Based off 11.6.3 example wordfreq.py on p.375-6
#
#
# Overall Plan:
# 1. Print introduction
# 2. Draw interface widgets/buttons
# 3. Draw window labels and entry boxes
# 4. Create output text object
# 5. Loop until Quit button is clicked
# 6. When Calculate button is clicked display child's estimated
#       adult height using hw7project2.py code
# 7. Activate Quit button after Calculate button is clicked to
#       allow user to exit and close program
#
#
# import the necessary python libraries and classes
# for this program none are needed

# ---Functions---
def printIntro():
    print("\nThis program analyzes the frequency of python reserved\n"
          "words in a python file and prints a report in order of\n"
          "most used to least used.\n")

# create list of all words in file
def fileTextList(filename):
    file = open(filename, 'r').read()
    # remove symbol chars
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = file.replace(ch, ' ')
    # split at whitespace to create list
    wordList = text.split()
    return wordList

# sort list of words by frequency count
def byFreq(pair):
    return pair[1]

# ---Main---
def main():
    printIntro()
    # get list of python reserved words
    reservedWords = fileTextList("reserved.txt")
    # prompt user for python file
    pythonFile = input("Python file to analyze: ")
    # get list of words in python file
    pyFileWords = fileTextList(pythonFile)

    # # get the sequence of words from the file
    # filename = input("File to analyze: ")
    # text = open(filename, 'r').read()
    # for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
    #     text = text.replace(ch, ' ')
    # text_word = text.split()

    # construct a dictionary of word counts
    counts = {}
    for word in pyFileWords:
        if word in reservedWords:
            counts[word] = counts.get(word, 0) + 1

    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)

    for i in range(len(counts)):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


if __name__ == '__main__':
    main()
