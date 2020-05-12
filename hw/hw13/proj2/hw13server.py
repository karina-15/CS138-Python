#! /usr/bin/python
#
# Homework No.  13
# Project No.   02
# File Name:    hw13server.py
# Programmer:   Karina Elias
# Date:         Dec. 12, 2019
#
# Problem Statement:
#   Reading for assignment:
#   http://docs.python.org/release/3.0.1/howto/sockets.html
#   https://docs.python.org/release/3.7.1/howto/sockets.html
#   Use the code here as a baseline.
#   http://www.bogotobogo.com/python/python_network_programming_server_client.php
#   Write a simple echo server and client. An echo server simply
#   sends back a response of what you sent. For example, you
#   should send a message to the server, the server prints out
#   the message and sends the message back to the client where
#   the client prints out the message.
#   Modify the server to send back the string in reverse order.
#
#   Run server first and while it is running run client and
#   enter message in client
#
#
# Overall Plan:
# 1. Create connection
# 2. Get message from user
# 3. Reverse message
# 4. Send message
# 5. Close connection
#
#
# import the necessary python libraries and classes
# for this program socket is used to make connections
# server.py
import socket

# reverse string input from user
def reverseString(message):
    # using join and predefined reversed
    reversedString = ''.join(reversed(message))
    return reversedString

def main():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    port = 12345
    # bind to the port
    s.bind((host, port))
    # queue up to 5 requests
    s.listen(5)
    # establish a connection
    clientsocket, addr = s.accept()
    # display connection made
    print("Connection from: {0}\n".format(str(addr)))

    # while connection to client is open
    while True:
        # receive message/data from client
        data = clientsocket.recv(1024).decode('ascii')
        # exit if connection is closed
        if not data:
            break
        # print reversed message/data
        data = reverseString(data)
        clientsocket.send(data.encode('ascii'))

    # close socket
    clientsocket.close()


if __name__ == '__main__':
    main()
