#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Parttime.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019

from Employee import Employee


class Parttime(Employee):
    def __init__(self, firstName, lastName, employeeID, numClasses):
        Employee.__init__(self, firstName, lastName, employeeID)
        self.numClasses = numClasses

    def getNumClasses(self):
        return self.numClasses

    def getPay(self):
        return self.numClasses * 1000

    def printInfo(self):
        return str("{0} {1:<9d} {2} {3} {4}".
          format(Employee.printInfo(self),
            self.getNumClasses(),
            '---'.ljust(11),
            '---'.ljust(10),
            self.getPay()))
