#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Salary.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019

from Employee import Employee

class Salary(Employee):
    def __init__(self, firstName, lastName, employeeID, salary):
        Employee.__init__(self, firstName, lastName, employeeID)
        self.salary = salary

    def getSalary(self):
        return self.salary

    def getPay(self):
        return self.salary

    def printInfo(self):
        return str("{0} {1} {2} {3} {4}".
          format(Employee.printInfo(self),
            '---'.ljust(9),
            '---'.ljust(11),
            '---'.ljust(10),
            self.getPay()))
