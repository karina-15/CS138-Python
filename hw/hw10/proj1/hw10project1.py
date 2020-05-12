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
# 2. Prompt user for python file
# 3. Create list of python file words
# 4. Create list of reserved python words
# 5. Create dictionary of reserved words and their frequency
# 6. Sort list of reserved words by count from most to least
# 7. Print results
#
#
# import the necessary python libraries and classes
# for this program regex is used to remove comments
import re


# ---FUNCTIONS---
def printIntro():
    print("\nThis program analyzes the frequency of python reserved\n"
          "words in a python file and prints a report in order of\n"
          "most used to least used.\n")


# create list of all words in file code
def fileTextList(filename):
    file = open(filename, 'r').read()
    # remove comments from python files
    # https://stackoverflow.com/a/28401921
    code = re.sub(r'(?m)^ *#.*\n?', '', file)
    # remove symbol chars from python files
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        cleanCode = code.replace(ch, ' ')
    # split at whitespace to create list
    wordList = cleanCode.split()
    return wordList


def createDictionary(wordsToCount, fileWords):
    counts = {}
    # runs through each word in python file
    for word in fileWords:
        # if word is a reserved word add to dictionary
        # if not already in dictionary otherwise,
        # increase count
        if word in wordsToCount:
            counts[word] = counts.get(word, 0) + 1
    return counts


# sort by count from highest to lowest frequency
def sort(dictionary):
    # create list of key-value pairs
    items = list(dictionary.items())
    items.sort()
    # byFreq sorts by value (count) not key (word)
    # reverse=True sorts from most to fewest
    items.sort(key = byFreq, reverse = True )
    return items


# sort list of words by frequency count instead of words
def byFreq(pair):
    return pair[1]


def printReport(dictionary, items):
    # print every word and its count in counts dictionary
    for i in range(len(dictionary)):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


# ---MAIN---
def main():
    printIntro()

    # ---INPUT---
    # prompt user for python file
    pythonFile = input("Python file to analyze: ")

    # ---PROCESS---
    # get list of words in python file code
    pyFileWords = fileTextList(pythonFile)
    # get list of python reserved words
    reservedWords = fileTextList("reserved.txt")
    # construct a dictionary of word counts
    counts = createDictionary(reservedWords, pyFileWords)
    # sort list of words by count from highest to lowest frequency
    items = sort(counts)

    # ---OUTPUT---
    printReport(counts, items)


if __name__ == '__main__':
    main()
