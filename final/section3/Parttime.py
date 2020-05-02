#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Parttime.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019

from finalEliasKarina.section3.Employee import Employee

class Parttime(Employee):
    def __init__(self, firstName, lastName, employeeID, numClasses):
        Employee.__init__(self, firstName, lastName, employeeID)
        self.numClasses = numClasses

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmployeeID(self):
        return self.employeeID

    def getNumClasses(self):
        return self.numClasses

    def getPay(self):
        return self.numClasses * 1000

    def printInfo(self):
        return str("Name: {0} {1}\tID: {2}\tNumber Classes: {3}\tPay:${4}".
                   format(self.getFirstName(),
                          self.getLastName(),
                          self.getEmployeeID(),
                          self.getNumClasses(),
                          self.getPay()))
