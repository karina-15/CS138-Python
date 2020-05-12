#! /usr/bin/python
# Homework No.  04
# Project No.   01
# File Name:    hw4project1.py
# Programmer:   Karina Elias
# Date:         Sep. 13, 2019
#
# Problem Statement:
# Write a program that uses the GUI to draw a simple picture
# with at least 3 graphical objects. Import graphics file
# (graphics.py)
#
#
# Overall Plan:
# 1. Create graphics window
# 2. Draw a red circle
# 3. Draw a green circle
# 4. Draw a blue circle
# 5. Draw a white rectangle for a label
# 6. Write text in white rectangle
# 7. Draw 2 yellow triangles on either side of label
# 8. Click to close window
#
#
# import the necessary python libraries
# import everything defined in graphics.py
from graphics import *


def main():
    # Create graphics window
    win = GraphWin("Simple Picture", 300, 300)
    win.setBackground("#333333")  # dark gray window background

    # Draws red circle
    red_circle = Circle(Point(100, 100), 70)
    red_circle.setOutline("#FF0000")
    red_circle.setFill("#FF0000")
    red_circle.draw(win)

    # Draws green circle
    green_circle = Circle(Point(200, 100), 70)
    green_circle.setOutline("#00FF00")
    green_circle.setFill("#00FF00")
    green_circle.draw(win)

    # Draws blue circle
    blue_circle = Circle(Point(150, 200), 70)
    blue_circle.setOutline("#0000FF")
    blue_circle.setFill("#0000FF")
    blue_circle.draw(win)

    # Draws white rectangle for text label
    rect = Rectangle(Point(70, 275), Point(230, 295))
    rect.setFill("#FFFFFF")
    rect.draw(win)

    # Draws bold text in center of white rectangle
    rect_label = Text(rect.getCenter(), "RGB circles")
    rect_label.setStyle("bold")
    rect_label.draw(win)

    # Draws yellow triangle on left side of label
    left_triangle = Polygon(Point(50, 275), Point(65, 295), Point(35, 295))
    left_triangle.setFill("#FFFF00")
    left_triangle.draw(win)

    # Draws yellow triangle on right side of label
    right_triangle = Polygon(Point(250, 275), Point(265, 295), Point(235, 295))
    right_triangle.setFill("#FFFF00")
    right_triangle.draw(win)

    # Close window with message located at top of window
    message = Text(Point(150, 15), "Click anywhere to close window")
    message.setTextColor("#FFFFFF")
    message.draw(win)
    win.getMouse()  # pause for click in window
    win.close()  # closes window


main()
