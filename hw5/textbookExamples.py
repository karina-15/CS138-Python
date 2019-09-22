#! /usr/bin/python
#
# STRING OPERATIONS - pg.125
#   +                       concatenation
#   *                       repetition
#   <string>[]              indexing
#   <string>[:]             slicing
#   len(<string>)           length
#   for <var> in <string>   iteration thru chars
#
# SOME STRING METHODS - pg.140
#   s.capitalize()              copy of s with only the 1st char capitalized
#   s.center(width)             copy of s centered in a field of given width
#   s.count(sub)                count the # of occurrences of sub in s
#   s.find(sub)                 find the 1st position where sub occurs in s
#   s.join(list)                concatenate list into a string, using s as
#                               separator
#   s.ljust(width)              like center, but s is left-justified
#   s.lower()                   copy of s in all lowercase char
#   s.lstrip()                  copy of s with leading white space removed
#   s.replace(oldsub,newsub)    replace all occurrences of oldsub in s with
#                               newsub
#   s.rfind(sub)                like find, but returns rightmost position
#   s.rjust(width)              like center, but s is right-justified
#   s.rstrip()                  copy of s with trailing white space removed
#   s.split()                   split s into a list of substrings
#                               (see example below)
#   s.title()                   copy of s w/ 1st char of ea. word
#                               capitalized
#   s.upper()                   copy of s w/ all chars convert to uppercase
#
# TYPE CONVERSION FUNCTIONS - pg.146
#   float(<expr>)   convert expr to a floating point value
#   int(<expr>)     convert expr to an integer value
#   str(<expr>)     return a string representation of expr
#   eval(<string>)  evaluate string as an expression
#
# STRING FORMATTING - pg.148
#   <template-string>.format(<values>)
#   {<index>:<format-specifier>}    # inside template-string where values go
#                                   # index not needed in Python 3.1
#                                   # index starts at 0 - l->r when omitted
#   <width>.<precision><type>       # in <format-specifier>
#                                   # width = space size of whole # value
#                                   # if value < width then fills w/ spaces
#                                   # if value > width then still shows full #
#                                   # width = 0 means use as much space as needed
#                                   # precision = 2 means round to 2 decimal places
#                                   # type char f means value should be a fixed pt #
#                                   # f means value should always show 2 decimal places even if 0
#
# STRING JUSTIFICATION - pg.150
#   <   # left justification
#   >   # right justification
#   ^   # center justification
# FILE PROCESSING - pg.154
#   <variable> = open(<name>, <mode>)   # create file object
#                                       # name = name of file on disk
#                                       # mode = r or w
#   <file>.read()       # returns entire remaining contents of file as a single large string
#   <file>.readline()   # returns next line of file, INCLUDING NEXT newline char
#   <file>.readlines()  # returns a LIST of remaining lines in file.
#                       # ea. list item is a single line INCLUDING newline char at END
#   print(..., file=<outputFile>)   # print to file, instead of Run screen


def main():
    # ---pg.122---
    # strings
    str1 = "Hello"
    str2 = 'spam'
    print(str1, str2)
    # Hello spam
    type(str1)
    # <class 'str'>
    type(str2)
    # <class 'str'>

    # ---pg.123---
    # string index
    greet = "Hello Bob"
    greet[0]
    # 'H'
    print(greet[0], greet[2], greet[4])
    # H l o
    x = 8
    print(greet[x - 2])
    # B

    # ---pg.124---
    # negative indexing = last characters
    greet[-1]
    # 'b'
    greet[-3]
    # 'B'

    # substrings/slicing
    # <string>[<start-int>:<end-int-not-included>]
    greet[0:3]
    # 'Hel'
    greet[5:9]
    # ' Bob'
    greet[:5]  # from start of string
    # 'Hello'
    greet[5:]  # til end of string
    # ' Bob'
    greet[:]  # entire string
    # 'Hello Bob'

    # ---pg.125---
    "spam" + "eggs"
    # 'spameggs'
    "Spam" + "And" + "Eggs"
    # 'SpamAndEggs'
    3 * "spam"
    # 'spamspamspam'
    "spam" * 5
    # 'spamspamspamspamspam'
    (3 * "spam") + ("eggs" * 5)
    # 'spamspamspameggseggseggseggseggs'
    len("spam")
    # 4
    len("SpamAndEggs")
    # 11
    for ch in "Spam!":
        print(ch, end=" ")
    # S p a m !

    # ---pg.128---
    # Lists also start @ index 0
    print()
    print("[1, 2] + [3, 4] -->", [1, 2] + [3, 4])
    print("[1, 2] * 3 -->", [1, 2] * 3)
    grades = ['A', 'B', 'C', 'D', 'F']
    print("grades = ['A', 'B', 'C', 'D', 'F']")
    print("grades[0] -->", grades[0])
    print("grades[2:4] -->", grades[2:4])
    print("len(grades) -->", len(grades))

    # ---pg.130---
    # Lists can be changed (Lists are mutable, strings are not)
    # Strings cannot be changed "in place"
    print("myList = [34, 26, 15, 10]")
    myList = [34, 26, 15, 10]
    print("myList[2] -->", myList[2])
    print("myList[2] = 0")
    myList[2] = 0
    print("myList -->", myList)
    print("myString = \"Hello World\"")
    myString = "Hello World"
    print("myString[2] -->", myString[2])
    print("myString[2] = 'z'")
    # myString[2] = 'z'     --> TypeError

    # ---pg.132---
    # Python uses Unicode over ASCII for more unique characters
    # Unicode includes all ASCII character #s
    # (ordinal) ord = char -> # code of char
    # chr = # code -> char
    print("ord(\"a\") -->", ord("a"))
    print("ord(\"A\") -->", ord("A"))
    print("chr(97) -->", chr(97))
    print("chr(90) -->", chr(90))
    print("chr(960) -->", chr(960))
    print("chr(8364) -->", chr(8364))

    # ---pg.135---
    # initialize empty string variable at beginning of program
    # accumulation variable
    message = ""

    # ---pg.136---
    # string split method
    myString = "Hello, string methods!"
    print("myString = ", myString)
    print("myString.split() -->", myString.split())

    print("\"32,24,25,57\".split(\",\") -->", "32,24,25,57".split(","))

    # ---pg.137---
    # eval examples
    # eval takes a string & evaluates it as a Python expression
    print("numStr = 500")
    numStr = "500"
    print("eval(numStr) -->", eval(numStr))
    print("eval(\"345.67\") -->", eval("345.67"))
    print("eval(\"3+4\") -->", eval("3+4"))
    print("x = 3.5")
    print("y = 4.7")
    x = 3.5
    y = 4.7
    print("eval(\"x * y\") -->", eval("x * y"))
    print("x = eval(input(\"Enter a number \"))")
    # commented out to keep program running to the end
    # x = eval(input("Enter a number "))
    # print("x -->", x)

    #  ---pg.139---
    # some string methods
    print("s = hello, I came here for an argument")
    s = "hello, I came here for an argument"
    print("s.capitalize() -->", s.capitalize())
    print("s.title() -->", s.title())
    print("s.lower() -->", s.lower())
    print("s.upper() -->", s.upper())
    print("s.replace(\"I\", \"you\") -->", s.replace("I", "you"))
    print("s.center(30) -->", s.center(30))
    print("s.center(50) -->", s.center(50))
    print("s.count('e') -->", s.count('e'))
    print("s.find(',') -->", s.find(','))
    print("\" \".join([\"Number\", \"one\", \"the\", \"Larch\"]) -->", " ".join(["Number", "one", "the", "Larch"]))
    print("\"spam\".join([\"Number\", \"one\", \"the\", \"Larch\"]) -->",
          "spam".join(["Number", "one", "the", "Larch"]))

    # list append
    print("squares = []")
    squares = []
    print("for x in range(1,101):\n\tsquares.append(x*x)")
    for x in range(1, 101):
        squares.append(x * x)
    print("squares = ", squares)

    # ---pg.144---
    # int, float conversions
    int("3")
    # 3
    float("3")
    # 3.0
    float("3.5")
    # 3.5
    # int("3.5")
    # returns ValueError

    # int, float leading zeros
    int("008")
    # 8
    int("05")
    # 5
    int("009")
    # 9
    # eval("05")
    # returns invalid token error

    # ---pg.146---
    # convert # to string
    str(500)
    # '500'
    value = 3.14
    str(value)
    # '3.14'
    print("The value is", str(value) + ".")
    # The value is 3.14.

    # ---pg.149---
    print("Hello {0} {1}, you may have won ${2}".format("Mr.", "Smith", 10000))
    # Hello Mr. Smith, you may have won $10000
    print("This int, {0:5}, was placed in a field of width 5".format(7))
    # This int,     7, was placed in a field of width 5
    print("This int, {0:10}, was placed in a field of width 10".format(7))
    # This int,          7, was placed in a field of width 10

    # not fixed-pt float = significant digits
    print("This float, {0:10.5}, has width 10 and precision 5".format(3.1415926))
    # This float,     3.1416, has width 10 and precision 5

    # fixed-pt gives # of decimal places
    print("This float, {0:10.5f}, is fixed at 5 decimal places".format(3.1415926))
    # This float,    3.14159, is fixed at 5 decimal places

    # not fixed-pt float = significant digits
    print("This float, {0:0.5}, has width 0 and precision 5".format(3.1415926))
    # This float, 3.1416, has width 0 and precision 5

    # if over value's decimal places, python fills in spaces w/ 0s
    print("Compare {0} and {0:0.20}".format(3.14))
    # Compare 3.14 and 3.1400000000000001243

    # ---pg.150---
    print("left justification: {0:<5}".format("Hi!"))
    print("right justification: {0:>5}".format("Hi!"))
    print("centered: {0:^5}".format("Hi!"))

    # ---pg.152---
    # \n means newline in Python
    # must use print to see newlines otherwise it displays
    # 'Hello\nWorld\n\nGoodbye 32\n'
    print("Hello\nWorld\n\nGoodbye 32\n")

    # ---pg.153---
    # file processing
    #   1. open file
    #   2. manipulate file
    #       read~input & write~output
    #   3. close file
    # to save file, after the above steps have been made
    #   create a new file w/ same name,
    #   write (modified) contents of memory in new file
    #   and closed new file

    # open file for reading
    infile = open("numbers.dat", "r")

    # readline() - only gets 1 line, always ends w/ newline char, input discards newline

    # prints 1st 5 lines of file
    #
    # inline = open(someFile, "r")
    # for i in range(5):
    #     line = infile.readline()
    #     print(line[:-1])  # removes newline at end of file string, w/o would have an extra newline
    #     # could also use print(line, end="") to remove 'print's newline

    # show file contents using readlines()
    # but large file can take up too much RAM
    #
    # infile = open(someFile, "r")
    # for line in infile.readlines():
    #     # process the line here
    # infile.close()

    # better way of looping thru file's lines
    # if no file w/ given name exists will create it
    # if file already exists it will be deleted & a new empty file will be created
    # infile = open(someFile, "r")
    # for line in infile:
    #     # process the line here
    # infile.close()

    # open file for output
    #
    # outfile = open("mydata.out", "w")


main()
