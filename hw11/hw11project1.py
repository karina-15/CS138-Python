#! /usr/bin/python
#
# Homework No.  11
# Project No.   01
# File Name:    hw11project1.py
# Programmer:   Karina Elias
# Date:         Dec. 11, 2019
#
# Problem Statement: Programming Exercise #1 p.423
#   Modify the Dice Poker program from this chapter to include
#   any or all of the following features: (chose (a) splash screen)
#   (a) Splash Screen. When the program first fires up, have
#       it print a short introductory message about the program
#       and buttons for "Let's Play" and "Exit." The main interface
#       shouldn't appear unless the user selects "Let's Play."
#   (b) Add a help button that pops up another window displaying
#       the rules of the game (the payoffs table is the most
#       important part).
#   (c) Add a high score feature. The program should keep track
#       of the 10 best scores. When a user quits with a good
#       enough score, he/she is invited to type in a name for
#       the list. The list should be printed in the splash screen
#       when the program first runs. The high-scores list will
#       have to be stored in a file so that it persists between
#       program invocations.
#
#
# Overall Plan:
# 1. Create SplashScreen class
# 2. Create window of same style as guipoker window
# 3. Add "Let's Play" and "Exit" buttons
# 4. Add button functionality to continue to pokerapp window
#       or exit program
# 5. Initialize in main
#
#
# import the necessary python libraries and classes
# for this program guipoker, pokerapp, and button are used
# from the textbook
# adds splash screen

from graphics import *
from guipoker import GraphicsInterface
from pokerapp import PokerApp
from button import Button

class SplashScreen:
    def __init__(self):
        # setup window name, size, background color
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        # setup dice poker label
        banner = Text(Point(300, 150), "Dice Poker")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        # setup message label
        msg = Text(Point(300, 200), "Welcome to Dice Poker")
        msg.setSize(18)
        msg.draw(self.win)
        # setup buttons
        self.playBtn = Button(self.win, Point(250, 360), 75, 35, "Let's Play")
        self.playBtn.activate()
        self.exitBtn = Button(self.win, Point(350, 360), 75, 35, "Exit")
        self.exitBtn.activate()

    # get button click
    def get_response(self):
        # while True keep window open
        while True:
            # get mouse click point or
            # keyboard entry
            p = self.win.checkMouse()
            k = self.win.checkKey()
            # play
            if p and self.playBtn.clicked(p) or k == "Return":
                self.win.close()
                return True
            # exit
            if p and self.exitBtn.clicked(p) or k == "Escape":
                self.win.close()
                return False

def main():
    # at start of program initialize splash screen
    splash = SplashScreen()
    # if playBtn is clicked, start GUI and run app
    if splash.get_response():
        inter = GraphicsInterface()
        app = PokerApp(inter)
        app.run()


if __name__ == '__main__':
    main()
