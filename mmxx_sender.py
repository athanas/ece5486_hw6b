import socket
import time
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
i = 0
while True:
    i=i+1
    sock.sendto(str(i),server_address)
    time.sleep(0.2)

