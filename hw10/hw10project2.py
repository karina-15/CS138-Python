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


# ---CLASSES---
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "J", "Q", "K"]
        self.suits = {'spade': 'spade.ppm',
                      'club': 'club.ppm',
                      'heart': 'heart.ppm',
                      'diamond': 'diamond.ppm'}
        filename = self.suits['spade']
        with open(filename, 'rb') as f:
            self.image = f.read()

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getImage(self):
        return self.image

class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("Card Display", 600, 400)
        self.win.setBackground("green")
        banner = Text(Point(300, 30), "Display a Card")
        banner.setSize(24)
        banner.setFill("yellow")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.textBox = Entry(Point(300, 75), 10)
        self.textBox.draw(self.win)
        self.displayCardButton = Button(self.win, Point(300, 115), 100, 20, "Display Card")
        self.displayCardButton.activate()   # after something is entered in text box
        # self.card = Rectangle(Point(225, 150), Point(375, 350))
        self.card = Image(Point(300, 200), 'heart.ppm')
        self.card.draw(self.win)
        self.msg = Text(Point(300, 380), "Welcome to the Card Display")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.win.getMouse()
        self.win.close()

# ---FUNCTIONS---

# ---MAIN---
def main():
    GraphicsInterface()


if __name__ == '__main__':
    main()
