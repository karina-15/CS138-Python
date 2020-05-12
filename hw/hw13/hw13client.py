#! /usr/bin/python
#
# Homework No.  13
# Project No.   02
# File Name:    hw13client.py
# Programmer:   Karina Elias
# Date:         Dec. 12, 2019
# client.py
import socket

def main():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    port = 12345
    # connection to hostname on the port.
    s.connect((host, port))
    # get input message from user
    msg = input("Enter a message or 'q' to quit: ")

    # while user does not quit
    while msg[0].lower() != 'q':
        s.send(msg.encode('ascii'))
        # Receive no more than 1024 bytes
        data = s.recv(1024).decode('ascii')
        print("Message received from server: {0}".format(data))
        msg = input("Enter a message or 'q' to quit: ")

    # close socket
    s.close()


if __name__ == '__main__':
    main()
