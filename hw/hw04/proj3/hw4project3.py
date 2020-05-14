#! /usr/bin/python
# Homework No.  04
# Project No.   03
# File Name:    hw4project3.py
# Programmer:   Karina Elias
# Date:         Sep. 13, 2019
#
# Problem Statement: Programming Exercise #8 p.119
# Line Segment Information
# This program allows the user to draw a line segment
# and then displays some graphical and textual
# information about the line segment.
#
#
# Overall Plan:
# 1. Create graphics window
# 2. Print introduction
# 3. Prompt user for 1st mouse click
#    start of line (x1, y1)
# 4. Prompt user for 2nd mouse click
#    end of line (x2, y2)
# 5. Draw line from #3 to #4
# 6. Calculate midpoint of line
#    midx = (x1 + x2)/2
#    midy = (y1 + y2)/2
# 7. Draw midpoint in color cyan
# 8. Calculate length of line
#    dx = x2 - x1
#    dy = y2 - y1
#    length = sqrt(((dx) ** 2) + ((dy) ** 2))
# 9. Calculate slope of line
#    slope = dy/dx
# 10. Display length and slope
# 11. Click to close window
#
#
# import the necessary python libraries
from graphics import *  # import everything defined in graphics.py
import math  # Makes math library available for sqrt()


def main():
    # Create graphics window
    win = GraphWin("Line Segment Information", 500, 500)
    win.setBackground("#333333")  # Dark grey window background

    # Print introduction
    intro1 = Text(Point(250, 15), "This program allows you to draw a line")
    intro1.setTextColor("#FFFFFF")
    intro1.draw(win)
    intro2 = Text(Point(250, 35), "and display its midpoint, length, and slope")
    intro2.setTextColor("#FFFFFF")
    intro2.draw(win)

    # ---Window Layout--- #

    # Create white rectangle for line drawing area
    line_canvas = Rectangle(Point(5, 45), Point(498, 460))
    line_canvas.setFill("#FFFFFF")
    line_canvas.draw(win)

    # Display label at bottom of window for user prompt and information
    info_label = Text(Point(250, 480), "Click anywhere in the white box to start the line")
    info_label.setTextColor("#FFFFFF")
    info_label.draw(win)

    # ---Input--- #
    # Get user click point and draw start point
    click1 = win.getMouse()
    x1 = click1.getX()
    y1 = click1.getY()
    point1 = Point(x1, y1)
    point1.draw(win)

    # Change display label at bottom of window
    info_label.setText("Click again to draw the line")

    # Get user's 2nd click
    click2 = win.getMouse()
    x2 = click2.getX()
    y2 = click2.getY()
    point2 = Point(x2, y2)

    # ---Process--- #
    # Draw line from user's clicks
    line = Line(point1, point2)
    line.setWidth(2)
    # line.setArrow("last")
    line.draw(win)

    # Calculate midpoint
    midx = (x1 + x2) / 2
    midy = (y1 + y2) / 2

    # Draw midpoint using circle
    midpoint = Circle(Point(midx, midy), 3)
    midpoint.setOutline("#00FFFF")
    midpoint.setFill("#00FFFF")
    midpoint.draw(win)

    # Calculate length
    dx = x2 - x1
    dy = y2 - y1
    length = round(math.sqrt((dx ** 2) + (dy ** 2)), 2)

    # Calculate slope
    slope = dy/dx
    # slope = "{0}/{1}".format(dy, dx)

    # ---Output--- #
    # Display results of length and slope
    results_text = "midpoint = ({0}, {1})" \
                   "   length = {2}" \
                   "   slope = {3}" \
                   "\nClick to exit".\
        format(round(midx, 2),
               round(midy, 2),
               round(length,2),
               round(slope, 2))
    info_label.setText(results_text)

    # Close window
    win.getMouse()  # pause for click in window
    win.close()


main()
