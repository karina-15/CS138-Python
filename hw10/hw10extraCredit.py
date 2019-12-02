#! /usr/bin/python
#
# Homework No.  10
# Project No.   Extra Credit
# File Name:    hw10extraCredit.py
# Programmer:   Karina Elias
# Date:         Nov. 22, 2019
#
# Problem Statement:
#   This program will create a GUI with a button and a picture.
#   The user will use the button to click through a complete
#   deck of cards starting with the club suit and rank 2-10,
#   Jack, Queen, King, and Ace. Use a dictionary as the storage
#   mechanism for suit and list for rank.
#
#
# Overall Plan:
# 1. Create a GUI window with a banner, "Card" button, rectangle
#       shape area to display card, and a "Quit" button
# 2. Create Card class with suit and rank display
# 3. Create Deck class to display the suit and rank of all Cards
#       in a list
# 4. When "Quit" button is clicked, close window
#
#
# import the necessary python libraries and classes
# for this program graphics is used
from graphics import *
from button import Button

# ---CLASSES---
class Card:
    def __init__(self, suit, rank):
        self.suit = Image(Point(300, 230), suit)
        self.rank = Text(Point(250, 155), rank)
        if suit == 'heart.ppm' or suit == 'diamond.ppm':
            self.rank.setTextColor('red')
        else:
            self.rank.setTextColor('black')
        self.rank.setSize(30)

    # draw suit image and rank text
    def show(self, win):
        self.suit.draw(win)
        self.rank.draw(win)

    # undraw image and text
    def clear(self):
        self.suit.undraw()
        self.rank.undraw()

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        # suit dictionary with images
        suit = dict(club='club.ppm',
                    heart='heart.ppm',
                    diamond='diamond.ppm',
                    spade='spade.ppm')
        # rank list
        rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # loop through each suit and rank to create a Card
        for image in suit:
            for val in rank:
                self.cards.append(Card(suit[image], val))

    # display each Card in a Deck
    def show(self, win, pt, quitButton, displayCardButton, rect):
        # while the Card button is clicked
        while not quitButton.clicked(pt) and displayCardButton.clicked(pt):
            # display all Cards in card list, change rectangle background,
            # and change Card button text
            for card in self.cards:
                if displayCardButton.clicked(pt):
                    rect.setFill('white')
                    displayCardButton.label.setText("Next Card")
                    displayCardButton.activate()
                    card.show(win)
                    pt = win.getMouse()
                    # check if "Quit" button was clicked
                    if not displayCardButton.clicked(pt) or quitButton.clicked(pt):
                        break
                    # undraw card so they don't overlap
                    card.clear()

# ---MAIN---
def main():
    # create GUI window
    win = GraphWin("Deck Display", 600, 400)
    # set window background to green
    win.setBackground("green")
    # create a title banner
    banner = Text(Point(300, 30), "Display Deck of Cards")
    banner.setSize(24)
    banner.setFill("yellow")
    banner.setStyle("bold")
    banner.draw(win)
    # create card display button
    displayCardButton = Button(win, Point(300, 90), 120, 25, "Display Card")
    displayCardButton.activate()
    # create a rectangle placeholder for card image
    rect = Rectangle(Point(225, 130), Point(375, 330))
    rect.setWidth(3)
    rect.draw(win)
    # create "Quit" button
    quitButton = Button(win, Point(300, 370), 120, 25, "Quit")
    quitButton.activate()
    # create a full Deck of cards
    deck = Deck()
    # get mouse click point
    pt = win.getMouse()
    # while the "Quit" button is not clicked
    while not quitButton.clicked(pt):
        # call show deck method
        deck.show(win, pt, quitButton, displayCardButton, rect)
        # check mouse click point again
        pt = win.getMouse()
    # close GUI window
    win.close()


if __name__ == '__main__':
    main()
