#!/usr/bin/env python 
import socket
from time import sleep
from random import random
from math import log

# Mean value of the processing rate of packets
MU = 50.0   # packets per second

# Create a buffer just large enough to hold one packet (queue size = 1)
RECV_BUF_SIZE = 10

# Model the exponential distribution generator for inter-packet delay
def exp_delay(x):
    return -log(1.0 - random())/x

# Create a socket for broadcasting: 
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.setsockopt( socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)
sock.setblocking(0)
sock.bind(('', 10000))

while True:
    # Receive from incoming, work (delay), and send out
    try: 
       data, address = sock.recvfrom(1024)
       # print("DATA: "+data+"  ADDR: "+str(address))
       sock.sendto(data, ('255.255.255.255', 10001))
       sleep(exp_delay(MU))
       while True: sock.recvfrom(1024)  # Flush pkts that came in while sleeping

    except socket.error:
       sleep(0.001)
       continue


