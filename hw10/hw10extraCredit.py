#! /usr/bin/python
#
# Homework No.  10
# Project No.   02
# File Name:    hw10project2.py
# Programmer:   Karina Elias
# Date:         Nov. 22, 2019
#
# Problem Statement:
#   This program will create a GUI with a text box, button
#   and a picture. The user will type in the suit of a card
#   (spade, club, heart, diamond) and it will show the
#   corresponding suit. Use a dictionary as the storage mechanism.
#
#
# Overall Plan:
# 1.
#
#
# import the necessary python libraries and classes
# for this program graphics is used
from graphics import *
from button import Button

# ---FUNCTIONS---

# ---MAIN---
def main():
    suit = {'club': 'club.ppm',
            'heart': 'heart.ppm',
            'diamond': 'diamond.ppm',
            'spade': 'spade.ppm'}
    win = GraphWin("Card Display", 600, 400)
    win.setBackground("green")
    banner = Text(Point(300, 30), "Display a Card")
    banner.setSize(24)
    banner.setFill("yellow")
    banner.setStyle("bold")
    banner.draw(win)
    textBox = Entry(Point(300, 75), 10)
    textBox.draw(win)
    displayCardButton = Button(win, Point(300, 115), 100, 20, "Display Card")
    displayCardButton.activate()  # after something is entered in text box
    rect = Rectangle(Point(225, 150), Point(375, 350))
    rect.draw(win)
    quitButton = Button(win, Point(300, 370), 100, 20, "Quit")
    quitButton.activate()

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if displayCardButton.clicked(pt) and textBox.getText() is not '':
            rect.setFill('white')
            inputText = textBox.getText()
            card = Image(Point(300, 250), suit[inputText])
            card.draw(win)
        pt = win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
