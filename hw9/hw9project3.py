#! /usr/bin/python
#
# Homework No.  09
# Project No.   03
# File Name:    hw9project3.py
# Programmer:   Karina Elias
# Date:         Oct 26, 2019
#
# Problem Statement: Programming Exercise #2 p.334
#   This program will use the Button class to create GUI for
#   hw7project2.py. Write a program that takes as input the
#   gender of the child, the height of the mother in inches
#   and the height of the father in inches. Output the estimated
#   adult height of the child in inches.  Convert this to feet,
#   and inches, ex. 63 inches = 5 feet 3 inches
#
#
# Overall Plan:
# 1. Create application window
# 2. Draw interface widgets/buttons
# 3. Draw window labels and entry boxes
# 4. Create output text object
# 5. Loop until Quit button is clicked
# 6. When Calculate button is clicked display child's estimated
#       adult height using hw7project2.py code
# 7. Activate Quit button after Calculate button is clicked to
#       allow user to exit and close program
#
#
# import the necessary python libraries and classes
# for this program graphics, button
from graphics import *
from cbutton import CButton


def main():

    # Create the application window
    win = GraphWin("Estimate Adult Height of Child", 275, 200)
    win.setCoords(0.0, 0.0, 5.0, 5.0)

    # Draw the interface widgets/buttons
    calculateButton = CButton(win, Point(2.5, 2.2), 0.63, "Calculate")
    calculateButton.activate()
    quitButton = CButton(win, Point(2.5, 0.5), 0.35, "Quit")

    # Draw window labels and entry boxes
    Text(Point(1.8, 4.5), "Enter child's gender:".ljust(25)).draw(win)
    genderEntry = Entry(Point(4.2, 4.5), 6)
    genderEntry.setFill("white")
    genderEntry.draw(win)
    Text(Point(1.8, 3.8), "Enter mother's height:".ljust(24)).draw(win)
    motherHeightEntry = Entry(Point(4.2, 3.8), 6)
    motherHeightEntry.setFill("white")
    motherHeightEntry.draw(win)
    Text(Point(1.8, 3.1), "Enter father's height:".ljust(26)).draw(win)
    fatherHeightEntry = Entry(Point(4.2, 3.1), 6)
    fatherHeightEntry.setFill("white")
    fatherHeightEntry.draw(win)

    # Create output text object
    adultHeightLabel = Text(Point(2.5, 1.4), "")
    adultHeightLabel.setStyle("bold")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        # calculate height only when calculate btn is clicked
        if calculateButton.clicked(pt):
            # clear output text once calculate btn is clicked
            adultHeightLabel.undraw()
            # ---INPUT--- #
            gender = genderEntry.getText()
            momHeight = eval(motherHeightEntry.getText())
            dadHeight = eval(fatherHeightEntry.getText())
            gender = gender[0].lower()
            # ---PROCESS--- #
            # same process from hw7project2.py
            if gender == 'm' or gender == 'b':
                adultH = ((momHeight * (13 / 12)) + dadHeight) / 2
            else:
                adultH = ((dadHeight * (12 / 13)) + momHeight) / 2
            # calculate height from inches to feet and inches
            feet = round(adultH) / 12
            inches = round(adultH) % 12
            # ---OUTPUT--- #
            adultHeightLabel.setText("\nAdult height: {2:.2f} inches = {0}'{1}\""
                                     .format(int(feet), int(inches), adultH))
            adultHeightLabel.draw(win)
            # allow quit btn to be clicked
            quitButton.activate()
        # get point/location where mouse was clicked
        pt = win.getMouse()
    # close window when Quit button is clicked
    win.close()


main()
