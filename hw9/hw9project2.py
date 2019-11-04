#! /usr/bin/python
#
# Homework No.  09
# Project No.   02
# File Name:    hw9project2.py
# Programmer:   Karina Elias
# Date:         Oct 26, 2019
#
# Problem Statement: Programming Exercise #7 p.335
#   This program will use a modified Button class that creates
#   circular buttons called CButton. The class will implement
#   the exact same methods that are in the Button class. The
#   constructor takes the center of the button and its radius
#   as normal parameters. Tested using roller.py.
#
#
# Overall Plan:
# 1. Create application window
# 2. Draw die
# 3. Draw circular buttons
# 5. Loop until Quit button is clicked
# 6. When Roll button is clicked, die face values change
# 7. Activate Quit button after Roll button is clicked to
#       allow user to exit and close program
#
#
# import the necessary python libraries and classes
# for this program graphics, button, random, dieview
# roller.py
# Graphics program to roll a pair of dice. Uses custom widgets
# CButton and DieView.

from random import randrange
from graphics import GraphWin, Point

from cbutton import CButton
from dieview import DieView


def main():
    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    # changed to CButton
    rollButton = CButton(win, Point(5, 4.2), 1.7, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(5, 1.2), 1.0, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()


main()
