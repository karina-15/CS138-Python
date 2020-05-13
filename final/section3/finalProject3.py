#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    finalProject3.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019
#
# Problem Statement:
#   This program will create a new Mira Costa Employee Management
#   system. There are 3 types of employees: Part-time Faculty,
#   Salary (include full time Faculty), and Hourly. You need to
#   create a generic employee which holds the employees first
#   and last name, and their id. The part-time faculty member
#   is paid a set amount(say 1000 per class) for each class they
#   teach. The salary employee is paid a monthly salary and the
#   hourly employee is paid based on the number of hours work
#   multiplied by their hourly rate.
#   The management system should allow you to enter a new employee,
#   remove an existing employee, save the existing employee
#   database to a file, load an existing employee database file,
#   and calculate the monthly paychecks for each employee. You
#   should use inheritance and polymorphism which is discussed
#   on page 419 (digital version of the book my vary slightly).
#
#
# Overall Plan:
# 1. Print introduction
# 2. Create Employee parent class
# 3. Create Parttime, Salary, Hourly child class
# 4. Create Management class with list of employee objects
# 5. Create file with employees information
# 6. Display employees information
#
#
# import the necessary python libraries and classes
# for this program None are used
from Management import Management
from Parttime import Parttime
from Salary import Salary
from Hourly import Hourly


# print introduction
def printIntro():
    print("\nThis program will create a MiraCosta Employee\n"
          "Management system\n")


# ---MAIN---
def main():
    printIntro()

    empList = []
    # create and add employees to list
    empList.append(Parttime("Luke", "Skywalker", len(empList), 5))
    empList.append(Salary("Han", "Solo", len(empList), 4000))
    empList.append(Hourly("Leia", "Organa", len(empList), 40, 15))
    empList.append(Hourly("Anakin", "Skywalker", len(empList), 35, 20))
    # create management list
    mccManagement = Management()
    mccManagement.addEmpList(empList)
    # write management to file
    mccManagement.writeFile("mccEmployees.txt")
    # display employees to console
    print('{0} {1} {2} {3} {4} {5} {6}'
        .format('-Name-'.ljust(7),
            ''.ljust(12),
            '-ID-'.ljust(7),
            '-Classes-'.ljust(10),
            '-Hours-'.ljust(8),
            '-Hourly Rate-'.ljust(14),
            '-Pay-'))
    for emp in mccManagement.getEmpList():
        print(emp.printInfo())
    print()


if __name__ == '__main__':
    main()
