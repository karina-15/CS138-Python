#! /usr/bin/python
#
# Homework No.  08
# Project No.   02
# File Name:    hw8project2.py
# Programmer:   Karina Elias
# Date:         Oct 20, 2019
#
# Problem Statement: Programming Exercise #14 p.265
#    Write a program that converts a color image to grayscale.
#    The user supplies the name of a file containing a GIF or
#    PPM image, and the program loads the image and displays
#    the file. At the click of the mouse, the program converts
#    the image to grayscale. The user is then prompted for a
#    filename to store the grayscale image in.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user for image filename
# 3. Display image
# 4. Convert the image to grayscale using p.265 pseudocode
# 5. Display grayscale image
# 6. Prompt user to enter new filename for grayscale image
#
#
# import the necessary python libraries
from graphics import *

def main():
    # Print introduction
    print("This program will convert a color image to grayscale.\n")

    # ---INPUT--- #
    imageFileName = input("Enter filename of image: ")
    print("Opening image to view...")
    img = Image(Point(0, 0), imageFileName)
    img = Image(Point(img.getWidth()/2, img.getHeight()/2), imageFileName)
    win = GraphWin("Image", img.getWidth(), img.getHeight())
    img.draw(win)

    # ---PROCESS--- #
    print("Click on image to convert to grayscale")
    win.getMouse()
    for row in range(img.getWidth()):
        for column in range(img.getHeight()):
            r, g, b = img.getPixel(row, column)
            brightness = int(round(0.229 * r + 0.587 * g + 0.114 * b))
            img.setPixel(row, column, color_rgb(brightness, brightness, brightness))
    # ---OUTPUT--- #
        update()
    saveFileName = input("Enter new filename to save grayscale image as: ")
    img.save(saveFileName)
    print("Click image window to exit program")

    win.getMouse()
    win.close()


main()
