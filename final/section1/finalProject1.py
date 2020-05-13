#! /usr/bin/python
#
# Final
# Project No.   01
# File Name:    finalProject1.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019
#
# Problem Statement:
#   This program will write a GUI that has 2 text boxes.
#   The first text box accepts a file to check the spelling.
#   The second file is the dictionary file or words.
#   When you click the spell-check button the program opens
#   both files reads the dictionary file into memory and then
#   spell checks the other file. To do the spell checking of
#   the other file you should do a binary search on the list
#   of words in the dictionary. If the word is not in the dictionary
#   file, print it on the screen as a potentially incorrect word.
#
#
# Overall Plan:
# 1. Create GUI with text boxes, labels, buttons
# 2. Create list of files words
# 3. Create list of dictionary words
# 4. Use binary search to compare misspelled words
# 5. Display misspelled words
#
#
# import the necessary python libraries and classes
# for this program graphics, button, and string
# are used for the GUI and word comparison
from final.section1.button import *
from graphics import *
from string import ascii_letters


# create GUI
class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("Spell Check", 600, 400, autoflush=False)
        # info labels
        instructLabel = Text(Point(300, 40), "Enter file names to check spelling")
        instructLabel.draw(self.win)
        fileToCheckLabel = Text(Point(150, 180), "File to check")
        fileToCheckLabel.draw(self.win)
        dictionaryFileLabel = Text(Point(450, 180), "Dictionary file")
        dictionaryFileLabel.draw(self.win)
        # file entry boxes
        self.fileToCheckEntry = Entry(Point(150, 200), 15)
        self.fileToCheckEntry.draw(self.win)
        self.dictEntryFile = Entry(Point(450, 200), 15)
        self.dictEntryFile.setText("english.txt")
        update()
        self.dictEntryFile.draw(self.win)
        # buttons
        self.fileToCheckBtn = Button(self.win, Point(150, 375), 90, 20, "Spell Check")
        self.fileToCheckBtn.activate()
        self.quitBtn = Button(self.win, Point(450, 375), 90, 20, "Quit")
        self.quitBtn.activate()
        self.inputs()

    # checks for button clicks
    # and file inputs
    def inputs(self):
        self.misspelledLabel = Text(Point(300, 250), "")
        self.misspelledLabel.draw(self.win)
        while True:
            mc = self.win.getMouse()
            # check file if clicked
            if self.fileToCheckBtn.clicked(mc):
                fileToCheckList = self.wordList(self.fileToCheckEntry.getText())
                dictList = self.wordList(self.dictEntryFile.getText())
                misspelled = self.misspelledWords(fileToCheckList, dictList)
                # display message if no misspelled words
                if not misspelled:
                    self.misspelledLabel.setText("No misspelled words")
                    update()
            # close program
            elif self.quitBtn.clicked(mc):
                break

    # create word list for files
    def wordList(self, filename):
        wordList = []
        with open(filename, 'r') as file:
            line = "".join([ch for ch in file.read() if ch in (ascii_letters + "'" + " " + "\n")])
            fileWordList = str.split(line)
            for word in fileWordList:
                wordList.append(word.lower())
        return wordList

    # display misspelled words to GUI
    def misspelledWords(self, fileToCheckList, dictList):
        misspelled = False
        misspelledList = []
        for word in fileToCheckList:
            misspelledWord = self.binarySearch(dictList, word)
            if misspelledWord is None:
                misspelledList.append(word)
                misspelled = True
            misspelledList.sort()
            self.misspelledLabel.setText('\n'.join(misspelledList))
            update()
        return misspelled

    # binary search on misspelled words
    # using algorithm from textbook
    def binarySearch(self, fileWordList, word):
        low = 0
        high = len(fileWordList) - 1
        while low <= high:
            mid = (low + high) // 2
            item = fileWordList[mid]
            if word < item:
                high = mid - 1
            elif word > item:
                low = mid + 1
            else:
                return mid


# ---MAIN---
def main():
    GraphicsInterface()


if __name__ == '__main__':
    main()
