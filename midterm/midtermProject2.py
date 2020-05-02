#! /usr/bin/python
#
# Homework No.  Midterm
# Project No.   02
# File Name:    midtermProject2.py
# Programmer:   Karina Elias
# Date:         Oct. 13, 2019
#
# Problem Statement:
#   This program will encode and decode Caesar ciphers.
#
#
# Overall Plan:
# 1. Print introduction
# 2. Prompt user whether to encode or decode
# 3. Prompt user for message
# 4. Prompt user for key
# 5. If encode was chosen use ord(ch) + key
# 6. Else decode using ord(ch) - key
# 7. Display encoded/decoded message
#
#
# import the necessary python libraries
# for this program none are needed


def main():
    # Print introduction
    print("\nThis program will encode and/or decode Caesar ciphers.")

    # ---INPUT--- #
    choice = -1
    messageList = []
    message2 = ''
    while choice != 0:
        choice = eval(input('\nChoose a number from below:'
                            '\n0. Exit'
                            '\n1. Enter message to encode'
                            '\n2. Enter message to decode'
                            '\nChoice: '))
    # ---PROCESS/OUTPUT---
        if choice == 1:
            key = eval(input('Enter key: '))
            message = input('Enter message to encode: ')
            for ch in message:
                if ord(ch) == 32:
                    messageList.append(' ')
                elif ord(ch) + key > 122:
                    messageList.append(chr(96 + ((ord(ch) + key) % 122)))
                elif ord(ch) + key > 90 and ord(ch) < 97:
                    messageList.append(chr(64 + ((ord(ch) + key) % 90)))
                else:
                    messageList.append(chr(ord(ch) + key))
            message2 = message2.join(messageList)
            print('Encoded message: ' + message2)

        elif choice == 2:
            key = eval(input('Enter key: '))
            message = input('Enter message to decode: ')
            for ch in message:
                if ord(ch) == 32:
                    messageList.append(' ')
                elif ord(ch) - key < 65:
                    messageList.append(chr((90 % ord(ch)) + 64 + key))
                elif 97 > ord(ch) - key > 90:
                    messageList.append(chr(((122 + key) % ord(ch)) + 96))
                else:
                    messageList.append(chr(ord(ch) - key))
            message2 = message2.join(messageList)
            print('Decoded message: ' + message2)

        else:
            print('Exiting...')
            break

        messageList.clear()
        message2 = ''


main()
