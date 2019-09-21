#! /usr/bin/python
#
# STRING OPERATIONS
# concatenation +
# repetition *
# indexing <string>[]
# slicing <string>[:]
# length len(<string>)
# iteration thru chars for <var> in <string>


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
    print(greet[x-2])
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
    greet[:5]   # from start of string
    # 'Hello'
    greet[5:]   # til end of string
    # ' Bob'
    greet[:]    # entire string
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

    # ---pg.134---






main()
