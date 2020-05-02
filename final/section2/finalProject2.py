#! /usr/bin/python
#
# Final
# Project No.   02
# File Name:    finalProject2.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019
#
# Problem Statement:
#   This program will read both the girl’s and boy’s files
#   into memory using a dictionary. The key should be the name
#   and value should be a user defined object which is the count
#   and rank of the name. Allow the user to input a name, the
#   program should find the name in the dictionary and print out
#   the rank and the number of namings. If the name isn’t a key
#   in the dictionary then the program should note this and say
#   that no match exists.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Create lists of names and number of names
# 3. Create dictionaries to rank lists' information
# 4. Ask for user input of a name
# 5. Display name information
#
#
# import the necessary python libraries and classes
# for this program None are used


# print introduction
def printIntro():
    print("\nThis program will find the rank and number of a\n"
          "popular name.\n")


# create lists from files
def getInfoFromFile(filename):
    nameList = []
    numList = []
    # open and read names from file
    with open(filename, 'r') as file:
        fileLines = file.readlines()
        for line in fileLines:
            itemList = line.split()
            nameList.append(itemList[0])
            numList.append(itemList[1])

    return nameList, numList


# create dictionaries
def setNameRank(nameList, numList):
    dictionary = {}
    for i in range(0, len(numList)):
        dictionary[nameList[i]] = i + 1, numList[i]
    return dictionary


# ---MAIN---
def main():
    printIntro()

    # create dictionaries
    girlNamesList, girlNumList = getInfoFromFile("girlnames.txt")
    girlsDictionary = setNameRank(girlNamesList, girlNumList)
    boyNamesList, boyNumList = getInfoFromFile("boynames.txt")
    boysDictionary = setNameRank(boyNamesList, boyNumList)

    # ask for user input
    name = input("Enter name: ")
    nameRank = girlsDictionary.get(name)
    # display name information
    if nameRank is None:
        print("{0} is not in the top 1000 girl names".format(name))
    else:
        print("{0} is #{1} in top 1000 girl names with {2} names.".
              format(name, girlsDictionary.get(name), girlsDictionary.get(name)))

    nameRank = boysDictionary.get(name)
    if nameRank is None:
        print("{0} is not in the top 1000 boy names".format(name))
    else:
        print("{0} is #{1} in top 1000 boy names with {2} names.".
              format(name, nameRank[0], nameRank[1]))


if __name__ == '__main__':
    main()
