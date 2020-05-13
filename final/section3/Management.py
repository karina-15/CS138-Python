#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Management.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019

from Employee import Employee
from Parttime import Parttime
from Salary import Salary
from Hourly import Hourly


class Management:
    def __init__(self):
        self.empList = []
        self.listSize = len(self.empList)

    def getEmpList(self):
        return self.empList

    def getListSize(self):
        return self.listSize

    def addEmp(self, emp):
        self.listSize += 1
        self.getEmpList().append(emp)

    def addEmpList(self, employees):
        for emp in employees:
            self.getEmpList().append(emp)

    def removeEmp(self, emp):
        self.getEmpList().remove(emp)

    # write management list to file
    def writeFile(self, filename):
        with open(filename, 'w') as file:
            file.write('{0} {1} {2} {3} {4} {5} {6}\n'
                .format('-Name-'.ljust(7),
                    ''.ljust(12),
                    '-ID-'.ljust(7),
                    '-Classes-'.ljust(10),
                    '-Hours-'.ljust(8),
                    '-Hourly Rate-'.ljust(14),
                    '-Pay-'))
            for emp in self.getEmpList():
                file.write(emp.printInfo())
                file.write("\n")

    # read management file
    def readFile(self, filename):
        empList = []
        hasNextLine = True
        # display header
        print(str("Retrieving employee type from file\n"
                  "{0} {1} {2}".
            format('-Name-'.ljust(7),
                   ''.ljust(11),
                   '-Employee Type-')))
        # while there are still employees in file
        while hasNextLine:
            with open(filename, 'r') as file:
                file.readline() # 1st line / headings
                # read rest of lines in file
                fileLines = file.readlines()
                # for every line
                for empLine in fileLines:
                    # separate the data by whitespace into list
                    empLineSplit = empLine.split()
                    # if length of line is only 3 columns
                    # employee type is default Employee
                    if len(empLineSplit) < 4:
                        empType = 'Employee'
                    # if 4th column (classes) is empty
                    # check 5th column (hours)
                    elif empLineSplit[3] == '---':
                        # if 5th column (hours) is empty
                        # employee type is salary
                        if empLineSplit[4] == '---':
                            empType = 'Salary'
                        # if 5th column (hours) contains info
                        # employee type is hourly
                        else:
                            empType = 'Hourly'
                    # if 4th column (classes) contains info
                    # employee type is parttime
                    else:
                        empType = 'Part-time'
                    # display employee name and type
                    empList.append(str("{0} {1} {2}".
                        format(empLineSplit[0].ljust(7),
                               empLineSplit[1].ljust(13),
                               empType)))
            # EOF is reached
            hasNextLine = False
        return empList