#!/usr/bin/python

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    print('Waiting for connection...')

    s.listen(1)
    c, addr = s.accept()

    print('Connection from: ' + str(addr))

    c.close()

if __name__ == '__main__':
    Main()
