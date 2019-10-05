#! /usr/bin/python
#
# Homework No.  07
# Project No.   01
# File Name:    hw7project1.py
# Programmer:   Karina Elias
# Date:         Oct 06, 2019
#
# Problem Statement: Programming Exercise #3 p.197
#   This program will calculate and print your grade. It takes
# the input is the percentage of
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user for sphere radius
# 3. Calculate the area (A=4*pi*r^2)
# 4. Calculate the volume (V=(4/3)*pi*r^3)
# 5. Display area and volume of sphere
#
#
# import the necessary python libraries
# math used for pi
import math


def sphereArea(radius):
    area = 4 * math.pi * radius ** 2
    return area


def sphereVolume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume


def main():
    # Print introduction
    print("This program will find the area and volume of a sphere.")

    # ---INPUT--- #
    radius = eval(input("Enter radius: "))

    # ---PROCESS/OUTPUT--- #
    print("Surface area of the sphere = {0:.2f}".format(sphereArea(radius)))
    print("Volume of the sphere = {0:.2f}".format(sphereVolume(radius)))


main()
