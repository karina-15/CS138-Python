#! /usr/bin/python
# Homework No.  06
# Project No.   03
# File Name:    hw6project3.py
# Programmer:   Karina Elias
# Date:         Sep. 30, 2019
#
# Problem Statement: Programming Exercise #2 p.196
# Write a program to print the lyrics for ten verses
# of "The Ants Go Marching."
#
#
# Overall Plan:
# 1. Print introduction
# 2. Display lyrics for "The Ants Go Marching." using functions
#
#
# import the necessary python libraries
# for this example none are needed

def printHurrah(numberStr):
    print("The ants go marching {0} by {0}, hurrah! hurrah!".format(numberStr))

def printAnt(numberStr):
    print("The ants go marching {0} by {0},".format(numberStr))


def printLittleOne(activity):
    print("The little one stops to {0},".format(activity))


def printBoom():
    print("And they all go marching down...")
    print("In the ground...\nTo get out...")
    print("Of the rain.\nBoom! Boom! Boom!")


def printVerse(numberStr, activity):
    printHurrah(numberStr)
    printHurrah(numberStr)
    printAnt(numberStr)
    printLittleOne(activity)
    printBoom()


def main():
    print()
    # Print introduction
    print("This program will print the lyrics to"
          "\n \"The Ants Go Marching\" using functions.\n")

    printVerse("one", "have some fun")
    printVerse("two", "ties his shoe")
    printVerse("three", "flick a flea")
    printVerse("four", "ask for more")
    printVerse("five", "look at a hive")
    printVerse("six", "pick up sticks")
    printVerse("seven", "talk to Devin")
    printVerse("eight", "greet a mate")
    printVerse("nine", "smell a pine")
    printVerse("ten", "go into the den")


main()
