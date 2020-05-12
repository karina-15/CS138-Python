#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Hourly.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019

from Employee import Employee


class Hourly(Employee):
    def __init__(self, firstName, lastName, employeeID, hours, hourlyRate):
        Employee.__init__(self, firstName, lastName, employeeID)
        self.hours = hours
        self.hourlyRate = hourlyRate

    def getHours(self):
        return self.hours

    def getHourlyRate(self):
        return self.hourlyRate

    def getPay(self):
        return self.hours * self.hourlyRate

    def printInfo(self):
      return str("{0} {1} {2:<12d} {3:<9d} {4}".
        format(Employee.printInfo(self),
          '---'.ljust(9),
          self.getHours(),
          self.getHourlyRate(),
          self.getPay()))
