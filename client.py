#!/usr/bin/python

def Main():
    host='127.0.0.1'
    port=5000

    s=socket.socket()
    s.connect((host, port))

    s.close()

if __name__ == '__main__':
    Main()
