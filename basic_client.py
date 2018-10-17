#!/usr/bin/env python
import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    try:
        message = raw_input(" -> ")  # take input
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response
            print('Received from server: ' + data)  # show in terminal
            message = raw_input(" -> ")  # again take input
    except KeyboardInterrupt:
        pass
    finally:
        client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()