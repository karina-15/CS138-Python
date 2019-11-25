#! /usr/bin/python
#
# Homework No.  12
# Project No.   01
# File Name:    hw12project1.py
# Programmer:   Karina Elias
# Date:         Nov. 24, 2019
#
# Problem Statement:
#   This program will compare the search times of linear
#   search and binary search for the list sizes of 1000,
#   10000, and 100000.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Create sorted lists of 1000, 10000, and 100000 random
#       integers
# 3. Get time to complete linear search
# 4. Get time to complete binary search
# 5. Print time comparisons
#
#
# import the necessary python libraries and classes
# for this program regex is used to remove comments
from time import *
from random import *

# ---FUNCTIONS---
def printIntro():
    print("\nThis program will compare the search times of\n"
          "linear search and binary search.\n")

def createList(itemNum):
    randList = [randint(0, itemNum) for x in range(itemNum)]
    randList.sort()
    return randList

def linearSearch(num, intList):
    start_time = perf_counter_ns()
    for i in range(len(intList)):
        if intList[i] == num:
            index = i
    index = -1
    return perf_counter_ns() - start_time

def binarySearch(num, intList):
    start_time = perf_counter_ns()
    low = 0
    high = len(intList) - 1
    while low <= high:
        mid = (low + high)//2
        item = intList[mid]
        if num == item:
            index = mid
        elif num < item:
            high = mid - 1
        else:
            low = mid + 1
    index = -1
    return perf_counter_ns() - start_time

def printSearchTimes(linearTime, binaryTime, items):
    # print every word and its count in counts dictionary
    print("{2} items\n"
          "Linear time = {0} ns\n"
          "Binary time = {1} ns\n"
          .format(linearTime, binaryTime, items))

# ---MAIN---
def main():
    printIntro()

    # ---INPUT---
    items1, items2, items3 = 1000, 10000, 100000
    list1, list2, list3 =\
        createList(items1), createList(items2), createList(items3)

    # ---OUTPUT---
    printSearchTimes(linearSearch(len(list1) + 1, list1),
                     binarySearch(len(list1) + 1, list1),
                     items1)
    printSearchTimes(linearSearch(len(list2) + 1, list2),
                     binarySearch(len(list2) + 1, list2),
                     items2)
    printSearchTimes(linearSearch(len(list3) + 1, list3),
                     binarySearch(len(list3) + 1, list3),
                     items3)


if __name__ == '__main__':
    main()
