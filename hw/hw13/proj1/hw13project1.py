#! /usr/bin/python
#
# Homework No.  13
# Project No.   01
# File Name:    hw13project1.py
# Programmer:   Karina Elias
# Date:         Dec. 12, 2019
#
# Problem Statement:
#   This program will verify the sort results. Compare the
#   sort times of python standard sort, selection sort and
#   merge sort for the list sizes of 5000, 50000, and 500000
#   (if this exceeds 30 minutes just put did not finish).
#
#
# Overall Plan:
# 1. Print introduction
# 2. Create sorted lists containing 5000, 50000, and 500000
#       random integers
# 3. Implement selection sort from book algorithm p.444
# 4. Implement merge sort from book algorithm p.445-6
# 5. Get time it takes to run each sort on each list
# 6. Print time comparisons
#
#
# import the necessary python libraries and classes
# for this program time and random is used
# to get the time it takes to run each search
from time import *
from random import *


# ---FUNCTIONS---
def printIntro():
    print("\nThis program will compare the search times of\n"
          "python's standard search, selection sort and merge\n"
          "search.\n")

# create a list of sorted random numbers
def createList(itemNum):
    randList = [randint(0, itemNum) for x in range(itemNum)]
    randList.sort()
    return randList

# implementation of selection sort - p.444
def selSort(nums):
    # sort nums into ascending order
    n = len(nums)

    # For each position in the list (except the very last)
    for bottom in range(n - 1):
        # find the smallest item in nums[bottom]..nums[n-1]
        mp = bottom  # bottom is smallest initially
        for i in range(bottom + 1, n):  # look at each position
            if nums[i] < nums[mp]:  # this one is smaller
                mp = i  # remember its index
        # swap smallest item to the bottom
        nums[bottom], nums[mp] = nums[mp], nums[bottom]

# implementation helper for merge sort - p.445-6
def merge(lst1, lst2, lst3):
    # merge sorted lists lst1 and lst2 into lst3
    # these indexes keep track of current position in each list
    i1 = i2 = i3 = 0
    n1, n2 = len(lst1), len(lst2)

    # Loop while both pieces have data
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:  # copy from lst1
            lst3[i3] = lst1[i1]
            i1 = i1 + 1
        else:  # copy from list2
            lst3[i3] = lst2[i2]
            i2 = i2 + 1
        i3 = i3 + 1  # item added to lst3

    # Here either lst1 or lst2 is done, One of the following loops will
    # execute to finish up the merge.

    # Copy remaining items (if any) from lst1
    while i1 < len(lst1):
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1
    # Copy remaining items (if any) from lst2
    while i2 < len(lst2):
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

# implementation of merge sort - p.447
# recursion on list of nums
def mergeSort(nums):
    # Put items of nums in ascending order
    n = len(nums)
    # Do nothing is nums contains 0 or 1 items
    if n > 1:
        # split into two sublists
        m = n // 2
        lst1, lst2 = nums[:m], nums[m:]
        # recursively sort each piece
        mergeSort(lst1)
        mergeSort(lst2)
        # merge the sorted pieces
        merge(lst1, lst2, nums)

# display comparisons of each algorithm
def printSearchTimes(standSortTime, selSortTime, mergeSort, items):
    # print every word and its count in counts dictionary
    print("{3} items\n"
          "Standard sort time = {0} s\n"
          "Selection sort time = {1} s\n"
          "Merge sort time = {2} s\n"
          .format(standSortTime, selSortTime, mergeSort, items))
    # write results of searches to hw12project1.txt file
    file = open("hw13project1.txt", 'a+')
    file.write("{3} items\n"
               "Standard sort time = {0} s\n"
               "Selection sort time = {1} s\n"
               "Merge sort time = {2} s\n\n"
               .format(standSortTime, selSortTime, mergeSort, items))
    file.close()


# ---MAIN---
def main():
    printIntro()

    # ---INPUT---
    # create lists of random integers
    items1, items2, items3 = 5000, 50000, 500000
    list1, list2, list3 = \
        createList(items1), createList(items2), createList(items3)

    # ---OUTPUT---
    # 5000 numbers
    # standard sort time
    standSortTime = perf_counter()
    list1.sort()
    standSortTime = perf_counter() - standSortTime
    # selection sort time
    selSortTime = perf_counter()
    selSort(list1)
    selSortTime = perf_counter() - selSortTime
    # merge sort time
    mergeSortTime = perf_counter()
    mergeSort(list1)
    mergeSortTime = perf_counter() - mergeSortTime
    # display time comparisons
    printSearchTimes(round(standSortTime, 2),
                     round(selSortTime, 2),
                     round(mergeSortTime, 2),
                     items1)

    # 50000 numbers
    # standard sort time
    standSortTime = perf_counter()
    list2.sort()
    standSortTime = perf_counter() - standSortTime
    # selection sort time
    selSortTime = perf_counter()
    selSort(list2)
    selSortTime = perf_counter() - selSortTime
    # merge sort time
    mergeSortTime = perf_counter()
    mergeSort(list2)
    mergeSortTime = perf_counter() - mergeSortTime
    # display time comparisons
    printSearchTimes(round(standSortTime, 2),
                     round(selSortTime, 2),
                     round(mergeSortTime, 2),
                     items2)

    # 500000 numbers
    # standard sort time
    standSortTime = perf_counter()
    list3.sort()
    standSortTime = perf_counter() - standSortTime
    # selection sort time
    selSortTime = perf_counter()
    selSort(list3)
    selSortTime = perf_counter() - selSortTime
    # merge sort time
    mergeSortTime = perf_counter()
    mergeSort(list3)
    mergeSortTime = perf_counter() - mergeSortTime
    # display time comparisons
    printSearchTimes(round(standSortTime, 2),
                     round(selSortTime, 2),
                     round(mergeSortTime, 2),
                     items3)


if __name__ == '__main__':
    main()
