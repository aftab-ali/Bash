#! /bin/python3

import socket

HOST = '127.0.0.1'
PORT = 2525

# AF_INET is IPV4
# SOCK_STREAM is for TCP
# SOCK_DGRAM is for UDP
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))


# To open a listening port on a host for incomming connections, use netcat
# nc -nvlp port_number


