#! /bin/python3

import socket

HOST = '127.0.0.1'
PORT = 2525

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))


