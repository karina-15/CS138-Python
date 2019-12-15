#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Employee.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019


class Employee:
    def __init__(self, firstName, lastName, employeeID):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmployeeID(self):
        return self.employeeID

    def printInfo(self):
        return str("Name: {0} {1}\tID: {2}".
                   format(self.getFirstName(),
                          self.getLastName(),
                          self.getEmployeeID()))
