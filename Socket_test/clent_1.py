__author__ = 'Hanz'
import socket, time

while True:
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.connect((host, port))
    print s.recv(1024)
    time.sleep(5)
