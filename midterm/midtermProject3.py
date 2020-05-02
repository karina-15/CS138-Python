#! /usr/bin/python
#
# Homework No.  Midterm
# Project No.   03
# File Name:    midtermProject3.py
# Programmer:   Karina Elias
# Date:         Oct. 13, 2019
#
# Problem Statement:
#   This program will create a connect the dots picture.
#
#
# Overall Plan:
# 1. Create graphics window
# 2. Print introduction
# 3. Create white rectangular canvas area
# 4. Display label at bottom of window to close window
# 5. Create while loop for up to 100 clicks
# 6. Get first mouse click
# 7. If user clicked in info_label area, close window
# 8. On first mouse click only draw the point with number label
# 9. Save first mouse click as previous point
# 10. On the next dots, draw a line from the previous point to
#       the current point
# 11. Draw a text label for the number next to the point when
#       clicked
# 12. Exit loop and close window until user clicks on info label
#       or 101 clicks are made
#
#
# import the necessary python libraries
from graphics import *  # import everything defined in graphics.py


def main():
    # Create graphics window
    win = GraphWin("Connect the dots", 607, 680)
    win.setBackground("#333333")  # Dark grey window background

    # Print introduction
    intro = Text(Point(303, 25), "This program allows you to create"
                                 "\na connect-the-dots picture with up to 100 dots")
    intro.setTextColor("#FFFFFF")
    intro.draw(win)

    # Create white rectangle for house drawing area
    draw_canvas = Rectangle(Point(5, 45), Point(605, 650))
    draw_canvas.setFill("#FFFFFF")
    draw_canvas.draw(win)

    # Display label at bottom of window for user prompt and information
    info_label = Text(Point(303, 665), "Click here to close window")
    info_label.setTextColor("#FFFFFF")
    info_label.draw(win)

    # ---PROCESS--- #
    mouseclicks = 1     # mouse click counter
    # while mouse click count is less than 100
    while mouseclicks != 101:
        dot = win.getMouse()
        # if user clicked info label break out of loop to close window
        if dot.getY() > 650:
            break
        # On the first mouse click draw the point and label only and save
        # as previous point
        if mouseclicks == 1:
            Point(dot.getX(), dot.getY()).draw(win)
            previousPoint = Point(dot.getX(), dot.getY())
        # Get current mouse click, draw a line connecting to previous
        # click, and set current click to previous
        else:
            currentPoint = Point(dot.getX(), dot.getY())
            currentPoint.draw(win)
            line = Line(previousPoint, currentPoint)
            line.setWidth(2)
            line.draw(win)
            previousPoint = currentPoint
        # Draw mouse click label near the point depending on how many digits
        if mouseclicks < 10:
            dot_label = Text(Point(dot.getX() + 8, dot.getY()), str(mouseclicks))
        elif mouseclicks == 100:
            dot_label = Text(Point(dot.getX() + 17, dot.getY()), str(mouseclicks))
        else:
            dot_label = Text(Point(dot.getX() + 13, dot.getY()), str(mouseclicks))
        dot_label.setTextColor('#000000')
        dot_label.draw(win)
        # increase mouseclick counter by 1
        mouseclicks += 1
    # While loop end

    # Close window
    win.close()


main()
