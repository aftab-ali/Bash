import sys
import socket
import threading
from queue import Queue


def tcp_scanner(_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.connect_ex((remote_server_IP, _port))
        if result == 0:
            print('Port {} OPEN'.format(port))
        sock.close()

    except socket.error:
        print("Couldn't connect to the server.")
        sys.exit()
    except KeyboardInterrupt:
        print('Exiting...')
        sys.exit()


# threading
def threader():
    while True:
        _port = _queue.get()
        tcp_scanner(_port)


def main():
    for x in range(100):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()
    for _port in range(100):
        _queue.put(_port)

    _queue.join()


if __name__ == '__main__':
    threading_lock = threading.Lock()
    _queue = Queue()
    try:
        remote_server = input('Enter Remote Server IP Address: ')
        remote_server_IP = socket.gethostbyname(remote_server)
        port_range = int(input('Enter the port range to scan from 1-65535: '))

    except socket.gaierror:
        print('Host name could not be resolved.')
        sys.exit()

    for port in range(port_range):
        tcp_scanner(port)
